'''
python爬虫-抓取微博页面搜索结果并写入文档中
'''
from selenium import webdriver
import xlwt
import time
driver=webdriver.Chrome()
driver.maximize_window()    #浏览器最大化
driver.get('https://s.weibo.com/')
driver.find_element_by_css_selector('#pl_homepage_search > div > div.searchbox > div > input[type=text]').send_keys('web自动化')
driver.find_element_by_css_selector('#pl_homepage_search > div > div.searchbox > button').click()
time.sleep(2)

#找到每个微博的标题，发帖人，发布时间，来源，收藏，转发，评论，点赞人数兵保存到excel文档中
wb=xlwt.Workbook()
sheet1=wb.add_sheet('sheet1')
sheet2=wb.add_sheet('sheet2')
sheet1.write(0,0,'标题')
sheet1.write(0,1,'发帖人')
sheet1.write(0,2,'发帖时间')
sheet1.write(0,3,'来源')
sheet1.write(0,4,'收藏数')
sheet1.write(0,5,'转发数')
sheet1.write(0,6,'评论数')
sheet1.write(0,7,'点赞数')

eles=driver.find_element_by_css_selector('div[action-type="feed_list_item"]')
counter=0
for ele in eles:
    counter+=1
    title=ele.find_element_by_css_selector('p[class="txt"]').text
    username=ele.find_element_by_css_selector('a[class="name"]').text
    time=ele.find_element_by_css_selector('p[class="from"]>a:nth-child(1)').text
    source=ele.find_element_by_css_selector('p[class="from"]>a:nth-child(2)').text
    coll_num=ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(1)').text
    forward_num=ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(2)').text
    coument_num=ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(3)').text
    like_num=ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(4)').text
    sheet1.write(counter, 0, title)
    sheet1.write(counter, 1, username)
    sheet1.write(counter, 2, time)
    sheet1.write(counter, 3, source)
    sheet1.write(counter, 4, coll_num)
    sheet1.write(counter, 5, forward_num)
    sheet1.write(counter, 6, coument_num)
    sheet1.write(counter, 7, like_num)

wb.save('weibo.xls')
driver.quit()
