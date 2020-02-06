'''
iframe元素定位
'''
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://login.anjuke.com/login/form')
#切换到iframe
iframeEle=driver.find_element_by_id('iframeLoginIfm')
driver.switch_to.frame(iframeEle)
driver.find_element_by_id('phoneIpt').send_keys('123456789')
#退出iframe回到主web页面
driver.switch_to.default_content()

