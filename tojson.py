# from pyecharts.charts import Bar
# bar = Bar()
# bar.add_xaxis(["a", "b", "c", "d", "e"])
# bar.add_yaxis("demo", [43, 58, 12, 88, 24])
# bar.render("demo.html")

#excel转json
import xlrd
import json
import operator
def read_xlsx(filename):
    # 打开excel文件
    data1 = xlrd.open_workbook(filename)
    # 读取第一个工作表
    table = data1.sheets()[5]
    # 统计行数
    n_rows = table.nrows
    data = []
    for v in range(4, n_rows - 1):
        # 每一行数据形成一个列表
        values = table.row_values(v)
        # 列表形成字典
        data.append({'salary': values[0],
                     'count': values[1],
                     })
    # 返回所有数据
    return data
if __name__ == '__main__':
    d = []
    d1 = read_xlsx('实习僧3.xlsx')
    d.extend(d1)
    #d = sorted(d, key=operator.itemgetter('time'))
    # 写入json文件
    with open('sxs3.json', 'w', encoding='utf-8') as f:
        # ensure_ascii=False显示中文,indent=2缩进为2
        f.write(json.dumps(d, ensure_ascii=False, indent=2))
