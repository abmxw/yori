import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["front.sans-serif"] = ["SimHei"]  # 设置字体


def 有序类别变量描述统计表(表名，变量名):
    result = 表名[变量名].value_counts(sort=False)
    描述统计图 = pd.DataFrame(result)
    描述统计图['比例'] = 描述统计图['count'] / 描述统计图['count'].sum()
    描述统计图['累计比例'] = 描述统计表['比例'].cumsum()
    return 描述统计表


def 绘制直方图(表名):
    x = 表名。index
    y = 表名['count'].values
    fig. ax2 = plt.subplots()
    ax2.bar(x, y)
    plt.show()