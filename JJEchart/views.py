from flask import flash,redirect,url_for,render_template

from JJEchart import app
import JJEchart.models as jjm
import datetime

from pyecharts import options as opts
from pyecharts.charts import Bar,Pie,Line



def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 8, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .reversal_axis()
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例"),
                         legend_opts=opts.LegendOpts(is_show=False))
    )
    return c

def pie_base() -> Pie:
    c = (
        Pie()
        .add(series_name="",
             data_pair=jjm.query_brand_count(),
             #data_pair = ['10','20','70'],
             radius=["40%","75%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="开业酒店数"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def line_base() -> Line:
    datestart = datetime.datetime.now().date()
    dt=[]
    i = 0
    while i < 7:
        dt.append(datestart.strftime('%m/%d'))
        datestart += datetime.timedelta(days=1)
        i+=1
    c = (
        Line()
            .add_xaxis(dt)
            #.add_yaxis("预订房晚", [20,70,0,90,80])
            .add_yaxis("预订房晚", jjm.query_rmnum_by_days())
            .add_yaxis("同比房晚", jjm.query_rmnum_by_lastyear_days())
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Line-面积图"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
        )
    )
    return c


@app.route('/',methods=['GET','POST'])
def index():
    # BiRepJours = BiRepJour.query.all()
    # return render_template('index.html',BiRepJours=BiRepJours)
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


@app.route("/pieChart")
def get_pie_chart():
    c = pie_base()
    return c.dump_options_with_quotes()

@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()