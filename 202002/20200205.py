from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com/')
time.sleep(2)
js='document.querySelector("#local_news > div.column-title-home > div").scrollIntoView()'
driver.execute_script(js)