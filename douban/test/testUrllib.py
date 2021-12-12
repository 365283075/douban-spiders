# -*- codeing = utf-8 -*-
# @time : 2021.9.7 17:44
# @Author: dltu
# @File : testUrllib.py
# @Software: PyCharm


import urllib.request

#获取一个get请求
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode("utf-8"))

#获取一个post请求

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data= data)
# print(response.read().decode("utf-8"))

# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("timeout")

response = urllib.request.urlopen("http://www.baidu.com")
#print(response.status)
# print(response.getheader("Server"))

# url = "http://www.douban.com"
# url = "http://httpbin.org/post"
# headers = {
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"
# }
# data = bytes(urllib.parse.urlencode({'name': 'eric'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "http://www.douban.com"
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"
}
req = urllib.request.Request(url=url,headers=headers,)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))