'''
selenium_keys
unittest-单元测试
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    #test1
    def test_baidu_search(self):
        driver=self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").send_keys("hello")
        driver.find_element_by_id("kw").send_keys(Keys.ENTER)    #键盘输入回车键
        time.sleep(2)
    #test2
    def test_bing_search(self):
        driver = self.driver
        driver.get("https://cn.bing.com/")
        driver.find_element_by_id("sb_form_q").send_keys("world")
        driver.find_element_by_id("sb_form_q").send_keys(Keys.ENTER)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

