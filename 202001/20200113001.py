'''
使用unittest写一个自动注册登录功能
'''
import time
import unittest
from selenium import webdriver

class cnode(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://39.107.96.138:3000/')

    def test_register(self):
        driver=self.driver
        driver.find_element_by_link_text('注册').click()
        driver.find_element_by_id('loginname').send_keys('test20200114')
        driver.find_element_by_id('pass').send_keys('20200113')
        driver.find_element_by_id('re_pass').send_keys('20200113')
        driver.find_element_by_id('email').send_keys('1976085713@qq.com')
        driver.find_element_by_xpath('//*[@id="signup_form"]/div[5]/input').click()
        time.sleep(2)

    def test_login(self):
        driver = self.driver
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_id('name').send_keys('testuser1')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="signin_form"]/div[3]/input').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.save_screenshot('./001.png')  #保存测试截图
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
