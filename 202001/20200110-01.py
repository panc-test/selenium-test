'''
assert
text
'''
import time
from selenium import webdriver
driver=webdriver.Chrome()

driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("hello world")
driver.find_element_by_id("su").click()

time.sleep(2)
result=driver.find_element_by_id("content_left").text
print(result)

assert "hello world"  in result
