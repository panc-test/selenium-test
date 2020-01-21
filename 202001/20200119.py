'''
xlrd库，读取excel表格内容
'''
import xlrd

#读取excel表格文件
data=xlrd.open_workbook('data.xlsx')

#获取所有sheet页名称
print(data.sheet_names())

# 获取一个工作表
sheet1=data.sheet_by_name('cefcifa')    #通过名称获取
sheet2=data.sheet_by_index(1)   #通过索引顺序获取
sheet3=data.sheets()[2] #通过索引顺序获取

print(sheet1.name, sheet2.name)

print('列数：',sheet1.ncols)
print('行数：',sheet1.nrows)

#打印输出第一行数据（列表形式）
print(sheet1.row_values(0))
#打印输出第一列数据（列表形式）
print(sheet1.col_values(1))

#返回单元格中的数据
value1=sheet1.cell_value(1,1)
value2=sheet1.cell(1,2).value
print(value1,value2)
print(type(value1),type(value2))

#遍历sheet1表格的所有数据
for x in range(sheet1.nrows):
    for y in range(sheet1.ncols):
        print(sheet1.cell_value(x,y))


