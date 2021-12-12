# -*- codeing = utf-8 -*-
# @time : 2021.9.7 11:27
# @Author: dltu
# @File : demo3.py
# @Software: PyCharm

'''
tup1 = ()
print(type(tup1))

tup2 = (50,)
print(type(tup2))

tup3 = (50,60,70)
print(type(tup3))



tup1 = ("abc","def",2000,2020)
print(tup1[0])
print(tup1[-1])
print(tup1[1:5]) #左闭右开
'''

'''

#增
tup1 = (12,34,56)
tup2 = ("a","b")

tup = tup1 + tup2
print(tup)

#删
tup1 = (12,34,56)
print(tup1)
del tup1
print("del")
print(tup1)

#改
#up1 = (12,34,56)
#tup1[0] = 100 #报错


#查
#开头

'''


#字典的定义
info = {"name":"吴彦祖","age":18}

'''
#字典的访问
print(info["name"])
print(info["age"])

#访问不存在的键
#print(info["gender"]) #直接访问会报错

#print(info.get("gdnder")) #none

print(info.get("age","20"))
print(info.get("gdnder","m"))
'''

'''
#增
info = {"name":"吴彦祖","age":18}
newID = input("输入新学号")
info["id"] = newID

print(info["id"])
'''


#删
'''
[del]
info = {"name":"吴彦祖","age":18}
print("前%s"%info["name"])

del info["name"]

print("后：%s"%info["name"])

info = {"name":"吴彦祖","age":18}
print("前%s"%info["name"])

del info

print("后：%s"%info)
'''

#[clear]

'''
info = {"name":"吴彦祖","age":18}
print("前%s"%info)

info.clear()

print("后：%s"%info)
'''

#改

'''
info = {"name":"吴彦祖","age":18}
print("前%s"%info)

info["age"] = 20

print("后：%s"%info)
'''

#查
'''
info = {"name":"吴彦祖","age":18}
print(info.keys()) #所有的键

print(info.values()) #所有的值

print(info.items()) #所有的对
'''
'''
#遍历所有的键
for key in info.keys():
    print(key)

#遍历所有的值
for value in info.values():
    print(value)

#遍历所有的对
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''

'''
#使用枚举函数，同时拿到下标和内容
mylist = ["a","b","c","d"]
print(enumerate(mylist))

for i,x in enumerate(mylist):
    print(i+1,x)
'''







