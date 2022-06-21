from django.test import TestCase

# Create your tests here.
import requests
 
url = "https://127.0.0.1:8000/recognize/uploadUrl"
myParams = {"imageUrl":"https://pic2.zhimg.com/v2-fe053de5b18e2feae0762da5783dad85_r.jpg"} # 字典格式，推荐使用，它会自动帮你按照k-v拼接url
res = requests.post(url=url, params=myParams)
 
print('url:',res.request.url)# 查看发送的url
print("response:",res.text)  # 返回请求结果

if __name__ == '__main__':
    print('test')