import sys
sys.path.append("ExcelLib\\jdcal-1.2")
sys.path.append("ExcelLib\\et_xmlfile-1.0.1")
sys.path.append("ExcelLib\\openpyxl-2.3.3")
import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(wb.get_sheet_names())

sheet3 = wb.get_sheet_by_name('Sheet3')
sheet3['A1'] = "John"

print(sheet3['A1'].value)

rec = "101,James,Pune"
reclst= rec.split(",")

for i in range(1,len(reclst)+1):
	cell = sheet3.cell(row=1,column=i)
	cell.value = reclst[i-1]

wb.save('example.xlsx')