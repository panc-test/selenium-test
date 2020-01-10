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

    def test_baidu_search(self):
        driver=self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").send_keys("hello")
        driver.find_element_by_id("kw").send_keys(Keys.ENTER)    #键盘输入回车键
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()