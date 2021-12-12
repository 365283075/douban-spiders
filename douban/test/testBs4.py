# -*- codeing = utf-8 -*-
# @time : 2021.9.10 16:19
# @Author: dltu
# @File : testBs4.py
# @Software: PyCharm

# Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.

# Tag
# NaviigavleString
# BeautifulSoup
# Comment

import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# print(bs.title)
# print(bs.a)
# print(bs.head)

# print(type(bs.head))

# 1.Tag 标签及其内容：拿到它找到的第一个内容


# print(bs.title.string)

# print(type(bs.title.string))

# 2.NavigableString 标签里的内容（字符串）

# print(bs.a.attrs)

# print(type(bs))

# #3.BeautifulSoup 表示整个文档

# print(bs.name)

# print(bs.attrs)

# print(bs)

# print(bs.a.string)
# print(type(bs.a.string))

# #4.Comment是一个特殊的NavigableString，输出不包含注释


# ---------------------------------------

# 文档的遍历

# print(bs.head.contents)
# print(bs.head.contents[1])

# 更多内容搜索文档

# 文档的搜索

# (1)find_all()
# 字符串过滤：查找与字符串完全匹配的内容

# t_list = bs.findAll("a")

# 正则表达式搜索：使用search()方法来匹配暖色
# t_list = bs.find_all(re.compile("a"))

# 方法：传入一个函数（方法），根据函数的要求来搜索(了解)
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
#
# for item in t_list:
#     print(item)


# print(t_list)

# 2.kwargs 参数

# t_list = bs.find_all(id="head")

# t_list = bs.find_all(class_=True)

# t_list = bs.find_all(href="http://news.baidu.com")

# for item in t_list:
#     print(item)

# 3.text参数

# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])

# t_list = bs.find_all(text=re.compile("\d")) #应用正则表达式来查找包含特点文本的内容（标签里的字符串）


# 4.limit 参数

# t_list = bs.find_all("a", limit=3)

# for item in t_list:
#     print(item)

# css选择器
# t_list = bs.select("title")   #通过标签来查找

# t_list = bs.select(".mnav")   #通过类名来查找

# t_list = bs.select("#u1")     #通过id来查找

# t_list = bs.select("a[class='bri']")#通过属性来查找

# t_list = bs.select("head>title")    #通过子标签来查找

t_list = bs.select(".mnav ~ .bri")  # 通过兄弟标签来查找

print(t_list[0].get_text())

# for item in t_list:
#     print(item)
