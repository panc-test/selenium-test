'''
处理excel表格的xlrd库
'''
import xlrd

#读取excel表格文件
data=xlrd.open_workbook('data.xlsx')

#获取所有sheet页名称
print(data.sheet_names())

# 根据sheet表的名称获取表的内容
sheet1=data.sheet_by_name('cefcifa')

print('列数：',sheet1.ncols)
print('行数：',sheet1.nrows)
#打印第一行数据（列表形式）
print(sheet1.row_values(0))
#打印第一列数据（列表形式）
print(sheet1.col_values(1))

#定位单元格数据，第一行第一列
value1=sheet1.cell_value(1,1)
print(value1)
print(type(value1))