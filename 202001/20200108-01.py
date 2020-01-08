'''
上传文件
'''

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_xpath('//*[@id="form"]/span[1]/span').click()
driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input')\
    .send_keys('E:\\Python\\PycharmProjects\\web_study\\tupian.jpg')