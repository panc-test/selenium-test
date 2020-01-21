'''
xlwt库，用于将内容写入excel
'''
import xlwt
from datetime import datetime

#定义格式
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()    #创建excel表格
ws = wb.add_sheet('A Test Sheet')   #创建一个sheet页

#往创建的sheet页里写入内容
ws.write(0, 0, '日期', style0)
ws.write(0, 1, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 2)
ws.write(2, 2, xlwt.Formula("A3+B3"))

#保存excel表格
wb.save('example.xls')
