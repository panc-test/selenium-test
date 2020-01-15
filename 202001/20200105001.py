'''
webdriver基本使用命令
'''

from selenium import webdriver  # 导入webdriver模块
from time import *

driver = webdriver.Chrome()  # 打开Google浏览器
driver.get("https://www.baidu.com")  # 打开 网址
# 打开本地 html页面
# driver.get(r"C:\Users\19760\Desktop\text.html")
title=driver.title  # 获取打开网址 的名字
url=driver.current_url  # 获取打开网址的 url
print('title:',title)
print('url:',url)

sleep(5)
driver.close() #关闭浏览器窗口
