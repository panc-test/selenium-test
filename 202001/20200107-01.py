'''
定位页面元素的方法
'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

# driver.find_element_by_id("kw").send_keys("web自动化")
# driver.find_element_by_name("wd").send_keys("web自动化")
# driver.find_element_by_css_selector("#kw").send_keys("web自动化")
# driver.find_element_by_css_selector("#u1 > a:nth-child(1)").click()
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('web自动化')

# driver.find_element_by_class_name("s_ipt").send_keys("hello")

#定位超链接
# driver.find_element_by_link_text("新闻").click()          --精确匹配
# driver.find_element_by_partial_link_text('新').click()      --模糊匹配
