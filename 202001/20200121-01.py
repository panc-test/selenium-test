'''
实例：将京东商城手机型号和价格保存到excel表格
'''
from selenium import webdriver
import xlwt

driver=webdriver.Chrome()
driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=e424a92e8d0d4845944e22ecb9a79534')

name=driver.find_elements_by_css_selector('div.p-name.p-name-type-2')
price=driver.find_elements_by_css_selector('div.p-price')

wb=xlwt.Workbook()
sheet1=wb.add_sheet('phones')
sheet1.write(0,0,'name')
sheet1.write(0,1,'price')
for index in range(len(name)):
    sheet1.write(index+1,0,name[index].text)
    sheet1.write(index+1,1,price[index].text)

wb.save('京东.xls')

driver.close()




