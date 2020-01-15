#Using Selenium to write tests

from selenium import webdriver
import unittest

class  NameTestCase(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome()
    def test1(self):
        pass
    def test2(self):
        pass
    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main()