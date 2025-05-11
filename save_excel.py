from openpyxl import Workbook

wb = Workbook()

ws = wb.active
print(ws.title)

wb.save(r"D:\Python workspace\test python\test.xlsx")