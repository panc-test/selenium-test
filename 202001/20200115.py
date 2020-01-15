'''
自动发帖
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class condeTest(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome()
        driver=self.driver
        driver.get('http://39.107.96.138:3000/')
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_id('name').send_keys('testuser1')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="signin_form"]/div[3]/input').click()


    def test_post_top(self):
        driver=self.driver
        driver.find_element_by_link_text('发布话题').click()
        driver.find_element_by_id('tab-value').click()
        driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()
        driver.find_element_by_id('title').send_keys('test自动发帖')

        content_area=driver.find_element_by_class_name('CodeMirror-scroll')
        content_area.click()
        ActionChains(driver).move_to_element(content_area).send_keys('1234567891233').perform()

        self.driver.save_screenshot('./002.png')
        driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[4]/input').click()

    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
