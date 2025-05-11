from openpyxl import load_workbook

wb = load_workbook(r"D:\Python workspace\test python\test.xlsx")
ws = wb.active

print(ws.title)

wb.save(r"D:\Python workspace\test python\test_bis.xlsx")