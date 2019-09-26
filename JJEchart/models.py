# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from JJEchart import Session
from sqlalchemy.orm import session,sessionmaker

Base = declarative_base()
myengine = sa.create_engine('sqlite:///D:/workspace/PycharmProjects/JJEchart/data.db')

class BiRepJour(Base):
    __tablename__="BI_REP_JOUR"
    code=sa.Column(sa.String(20),primary_key=True)
    sta_des=sa.Column(sa.String(2))
    biz_date=sa.Column(sa.DateTime)
    create_datetime=sa.Column(sa.DateTime)
    descript=sa.Column(sa.String(60))
    PRODUCTION_TTL=sa.Column(sa.Float)
    PRODUCTION_RM=sa.Column(sa.Float)
    REVPAR=sa.Column(sa.Float)
    ADR=sa.Column(sa.Float)
    OCC=sa.Column(sa.Float)
    MON_PRODUCTION_RM_BUDGET=sa.Column(sa.Float)
    MON_REVPAR_BUDGET=sa.Column(sa.Float)
    MON_ADR_BUDGET=sa.Column(sa.Float)
    MON_OCC_BUDGET=sa.Column(sa.Float)
    country_des=sa.Column(sa.String(60))
    province_des = sa.Column(sa.String(60))
    city_des=sa.Column(sa.String(60))
    brand_des=sa.Column(sa.String(60))
    brand_view=sa.Column(sa.String(60))
    area1_des=sa.Column(sa.String(60))
    area2_des=sa.Column(sa.String(60))
    server_name=sa.Column(sa.String(60))

def query_brand_count():
    Session.config(autocommit=False, autoflush=False, bind=myengine)
    session = Session()
    rs = session.query(BiRepJour.brand_view,sa.func.count(BiRepJour.brand_view)).filter(
        BiRepJour.brand_view != None).group_by(BiRepJour.brand_view).all()
    return rs
