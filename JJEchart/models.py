# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy.sql import func

from JJEchart import app

Base = declarative_base()
# eng = sa.create_engine('sqlite:///D:/workspace/PycharmProjects/JJEchart/JJEchart/data.db?check_same_thread=False')
# eng = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI']+'?check_same_thread=False')
eng = sa.create_engine("mysql://root:Password@localhost/mid",pool_pre_ping=True,pool_recycle=1)
connection = eng.connect()
metadata = sa.MetaData()

BiRepJour = sa.Table(
    'BI_REP_JOUR',metadata,
    sa.Column('code',sa.String(20),primary_key=True),
    sa.Column('sta_des',sa.String(2)),
    sa.Column('biz_date',sa.DateTime),
    sa.Column('create_datetime',sa.DateTime),
    sa.Column('descript',sa.String(60)),
    sa.Column('PRODUCTION_TTL',sa.Float),
    sa.Column('PRODUCTION_RM',sa.Float),
    sa.Column('REVPAR',sa.Float),
    sa.Column('ADR',sa.Float),
    sa.Column('OCC',sa.Float),
    sa.Column('MON_PRODUCTION_RM_BUDGET',sa.Float),
    sa.Column('MON_REVPAR_BUDGET',sa.Float),
    sa.Column('MON_ADR_BUDGET',sa.Float),
    sa.Column('MON_OCC_BUDGET',sa.Float),
    sa.Column('country_des',sa.String(60)),
    sa.Column('province_des',sa.String(60)),
    sa.Column('city_des',sa.String(60)),
    sa.Column('brand_des',sa.String(60)),
    sa.Column('brand_view',sa.String(60)),
    sa.Column('area1_des',sa.String(60)),
    sa.Column('area2_des',sa.String(60)),
    sa.Column('server_name',sa.String(60))
)




def query_brand_count():
    with eng.connect() as con:
        s = sa.select([BiRepJour.c.brand_view, func.count(BiRepJour.c.code).label('num_brand')]).where(
            BiRepJour.c.brand_view != None).group_by("brand_view")
        result = connection.execute(s)
    return result

'''
获取当日新增订单数
'''
def query_resv_today_count():
    with eng.connect() as con:
        result = connection.execute("SELECT count(1) as count FROM master_base_bs \
                                    WHERE hotel_group_id=1 AND rsv_id in(0,id) AND rsv_class<>'H' \
                                    AND DATE(create_datetime)>=DATE('2019-08-27') AND DATE(create_datetime)<=DATE('2019-09-27') \
                                    group by DATE(create_datetime)")
    return result

'''
获取7日，按日分组订单间夜数，订单数
'''
def query_rmnum_by_days():
    rows=[]
    with eng.connect() as con:
        result = connection.execute("SELECT SUM(rmnum) as rmnum FROM \
                (SELECT (@rownum := @rownum - 1) AS ROWNUM, DATE_ADD(n.today,INTERVAL -1 * @rownum DAY) DAYS \
                FROM master_base t,(SELECT @rownum := 7) r,(SELECT CURDATE() today) n LIMIT 0, 7) a \
                LEFT JOIN master_base b ON a.days BETWEEN b.arr AND b.dep \
                WHERE b.hotel_group_id=1 AND b.rsv_id IN(0,b.id) AND b.rsv_class<>'H' AND b.sta IN('R','I','O') \
                GROUP BY a.days")
        for row in result:
          rows.append(row[0])
        return rows

'''
去年同期
7日，按日分组订单间夜数，订单数
'''
def query_rmnum_by_lastyear_days():
    rows=[]
    with eng.connect() as con:
        result = connection.execute("SELECT SUM(rmnum) FROM \
                (SELECT (@rownum := @rownum - 1) AS ROWNUM, DATE_ADD(n.today,INTERVAL -1 * @rownum DAY) DAYS \
                FROM master_base t,(SELECT @rownum := 7) r,(SELECT DATE_ADD(CURDATE(),INTERVAL -1 YEAR) today) n LIMIT 0, 7) a \
                LEFT JOIN master_base b ON a.days BETWEEN b.arr AND b.dep \
                WHERE b.hotel_group_id=1 AND b.rsv_id IN(0,b.id) AND b.rsv_class<>'H' AND b.sta IN('R','I','O') \
                GROUP BY a.days")
        for row in result:
          rows.append(row[0])
        return rows
