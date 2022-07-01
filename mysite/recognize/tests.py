# from django.test import TestCase

# # Create your tests here.
# import requests
 
# my_headers = [
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
#     'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#     'Opera/9.25 (Windows NT 5.1; U; en)',
#     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#     'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
#     'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
#     "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
#     "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
# ]

# url = "http://127.0.0.1:8000/recognize/uploadUrl"
# myParams = {"imageURL":"https://pic2.zhimg.com/v2-fe053de5b18e2feae0762da5783dad85_r.jpg"} # 字典格式，推荐使用，它会自动帮你按照k-v拼接url
# res = requests.post(url=url, data=myParams)
 
# print('url:',res.request.url)# 查看发送的url
# print("response:",res.text)  # 返回请求结果
import json
import os
import requests
import time
 
str_d = {"b": "b_image", "d": "b_image", "f": "f_image",
       "l": "l_image", "r": "r_image", "u": "t_image"}
 
# 文件夹地址
filepath = r'D:\\1GRADUATED\\WEB\\Githubpro\\gongxiangbei2022\\PlantRecognizeServer\\mysite\\static\\other\\yueji.jpeg'
 
# 传入的数据
dit = {'image': ('yueji.jpeg', open(filepath, "rb"), 'image/jpeg', {})}
 
 
 
# 测试时间
start = time.process_time()
 
# 调用接口网址：网址是假的，如果使用，请修改网址
url = 'http://127.0.0.1:8000/recognize/uploadImage'
 
# data如果没有，可以不写
res = requests.post(url, files = dit)
obj = json.loads(res.text)
string = json.dumps(obj, ensure_ascii=False)
# end = time.process_time()
 
# # 计算接口调用时间
# if res.status_code == 200:
#     print(end - start)
 
# 返回数据
print(string)
 