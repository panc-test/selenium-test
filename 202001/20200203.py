'''
鼠标键盘操作单击、双击、点击鼠标右键、拖拽
特殊键操作
'''
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
#打开网址并登录操作
driver.get('http://39.107.96.138:3000/')
driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[6]').click()
driver.find_element_by_css_selector('#name').send_keys('testuser1')
driver.find_element_by_css_selector('#pass').send_keys('123456')
driver.find_element_by_class_name('span-primary').click()
# driver.find_element_by_class_name('span-primary').send_keys(Keys.ENTER)

driver.find_element_by_class_name('span-success').click()
time.sleep(2)

#模拟快捷键ctrl+b操作
text_area=driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[6]')
action=ActionChains(driver)
action.move_to_element(text_area).click()
action.key_down(Keys.CONTROL)
action.send_keys('b')
action.key_up(Keys.CONTROL)
action.perform()


