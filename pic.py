from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot


def time_sequence_pic(time_series_df):
    """
    绘制时序图
    :param time_series_df: df
    :return:
    """

    str_columns = time_series_df.columns
    x = list(time_series_df[str_columns[0]].astype('str'))
    y = list(time_series_df[str_columns[1]].astype('float'))

    line1 = Line(init_opts=opts.InitOpts(width='1200px', height='500px', bg_color="white"))
    line1.set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                          tooltip_opts=opts.TooltipOpts(is_show=True, trigger='axis', axis_pointer_type='cross'),
                          title_opts=opts.TitleOpts(title=str_columns[1]))

    line1.add_xaxis(x)
    line1.add_yaxis(y_axis=y, series_name=str_columns[1], label_opts=opts.LabelOpts(is_show=True, font_size=7))

    return line1

def data_distribution_pic(data_distribution_df):
    """
    绘制指标分布
    :param data_distribution_df: df
    :return:
    """
    x = list(data_distribution_df.loc['interval', :].astype('str'))
    y = list(data_distribution_df.loc['frequency_rate', :].astype('float'))
    # colors = ['#c23531'] * (len(x) - 1) + ['#2f4554']
    colors = ['#c23531'] * len(x)

    data_pair = []
    for k, v, c in zip(x, y, colors):
        data_pair.append(
            opts.BarItem(
                name=k,
                value=v,
                itemstyle_opts=opts.ItemStyleOpts(color=c)
            ))

    bar1 = Bar(init_opts=opts.InitOpts(width='1400px', height='500px', bg_color="white"))
    bar1.set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                         tooltip_opts=opts.TooltipOpts(is_show=True, trigger='axis', axis_pointer_type='cross'),
                         title_opts=opts.TitleOpts(title=" "),
                         xaxis_opts=opts.AxisOpts(name='区间'),
                         yaxis_opts=opts.AxisOpts(name='频率')
                         )
    bar1.add_xaxis(
        x
    )
    bar1.add_yaxis(
        "",
        data_pair,
        itemstyle_opts=opts.ItemStyleOpts(color=colors[0]),
        # label_opts = opts.LabelOpts(is_show=True),
        label_opts=opts.LabelOpts(is_show=True, formatter="{c}%", font_size=7),
        category_gap="0%"
    )

    return bar1