'''
查找多个元素
'''

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=e424a92e8d0d4845944e22ecb9a79534')
time.sleep(2)
#查找多个元素
eles=driver.find_elements_by_css_selector('li.gl-item div.p-price')
print(type(eles))
print(eles[0])
print(eles[0].text)

for x in range(len(eles)):
    print(eles[x].text)

driver.close()