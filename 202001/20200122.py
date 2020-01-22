'''
调用百度ocr接口识别图片验证码
https://ai.baidu.com/ai-doc/OCR/zk3h7xz52
'''
from selenium import webdriver
import time
import requests
import base64,urllib,urllib3

#保存图片验证码
driver=webdriver.Chrome()
driver.get('https://persons.shgjj.com/gjjweb/#/login5/A0')
time.sleep(5)   #不加等待时间可能会定位不到元素
image=driver.find_element_by_xpath('//*[@id="mobilephone"]/form/div[2]/div[2]/img')
image.screenshot('./image.png')

#调用鉴权接口获取token值
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xl4rRe3hGhgHqsUHWjNRUQxG&client_secret=aX35jYgl3mUEWyqDfWvG9lGdxQmQZk08'
response1= requests.get(host)
r=response1.json()
print(r)
access_token=r['access_token']
print('access_token=',access_token)

#post请求百度ocr上传图片识别验证码
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token="+access_token   #请求url

f = open('./image.png', 'rb')   # 参数rb二进制方式打开图片文件
img = base64.b64encode(f.read())    #将图片经过base64编码成一串字符串
params = {"image":img}  #字典键值对

response2 = requests.post(request_url, data=params)    #发送post请求
image_jion=response2.json()
print('image_jion=',image_jion)
image_num=image_jion['words_result'][0]['words']  #获取图片验证码


driver.find_element_by_xpath('//*[@id="mobilephone"]/form/div[2]/div[1]/input').send_keys(image_num)
