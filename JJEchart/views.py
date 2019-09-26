from flask import flash,redirect,url_for,render_template

from JJEchart import app
import JJEchart.models as jjm

from jinja2 import Markup
from pyecharts import options as opts
from pyecharts.charts import Bar,Pie



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
             radius=["40%","75%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
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