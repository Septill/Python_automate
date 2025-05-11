from openpyxl import Workbook

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

ws.auto_filter.ref = "a1:d7"
ws.auto_filter.add_filter_column(1,["50","88"])
ws.auto_filter.add_sort_condition("c2:d7",True)

wb.save(r"D:\Python workspace\test python\test_filter.xlsx")

import pandas as pd

df = pd.read_excel(r"D:\Python workspace\test python\test_filter.xlsx")
df_value = df.sort_values(by="Peach", ascending= True)

writer = pd.ExcelWriter(r"D:\Python workspace\test python\test_filter_bis.xlsx")
df_value.to_excel(writer, sheet_name= "test_filter_bis", index=False) # remove index !!

writer.close()