'''
selenium.webdriver.common.keys
TEXT
ASSERT
'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("hello world")
#driver.find_element_by_id("su").click()
driver.find_element_by_id('kw').send_keys(Keys.ENTER)

time.sleep(2)
result=driver.find_element_by_id("content_left").text
print(result)

assert "hello world"  in result
