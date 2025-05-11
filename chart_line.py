from openpyxl import Workbook
from openpyxl.chart import Reference, LineChart

wb = Workbook()
ws = wb.active

rows = [
    ["Month","Peach","Grappe","Apple"],
    [1,38,28,59],
    [2,88,52,36],
    [3,50,23,65],
    [4,21,57,56],
    [5,9,12,36],
    [6,45,48,36]
]

for row in rows:
    ws.append(row)

c1 = LineChart()
c1.title = "Fruits Sales Chart"
c1.style = 13
c1.y_axis.title = "Quantities"
c1.x_axis.title = " Month"

data = Reference (ws,min_row = 1, max_row= 7, min_col=2, max_col= 4 ) # attention the indexs

c1.add_data(data, titles_from_data = True)

s0 = c1.series[0]
s0.marker.symbol = "triangle"
s0.marker.graphicalProperties.solidFill = "FF0000"
s0.marker.graphicalProperties.line.solidFill = "0000FF"

s1 = c1.series[1]
s1.graphicalProperties.line.solidFill = "00AAAA" 
s1.graphicalProperties.line.dashStyle = "sysDot"
s1.graphicalProperties.line.width = 80000

s2 = c1.series[2]
s2.smooth = True

ws.add_chart(c1, "a8")

wb.save(r"D:\Python workspace\test python\test_chart.xlsx")