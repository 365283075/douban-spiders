# -*- codeing = utf-8 -*-
# @time : 2021.9.7 13:29
# @Author: dltu
# @File : demo1.py
# @Software: PyCharm


'''
#函数的定义
def printinfo():
    print("-----------")
    print("--人生苦短--")
    print("-我用Python-")
    print("-----------")

#函数的调用

printinfo()
'''

'''
#带参数的函数
def add2Num(a,b):
    c = a + b
    print(c)

add2Num(1,2)
'''

'''
def add2Num(a,b):
    return a+b #通过return来返回结果


result = add2Num(1,2)
print(result)
print(add2Num(11,22))
'''

#返回多个值的函数
'''
def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu #多个返回值用逗号分割

sh,yu = divid(5,2)    #用多个值来保存返回内容

print("shang:%d,yu:%d"%(sh,yu))
'''

'''
def hengxian():
    print("-"* 30)

def duohang():
    i = 0
    x = int(input("请输入："))
    while i < x:
        hengxian()
        i += 1

duohang()
'''

'''
def count(a,b,c):
    he = a+b+c
    return he

def average(a,b,c):
    sumResult = count(1,2,3)
    aveResult = sumResult/3.0
    return aveResult

y = average(1,2,3)

print(y)
'''

#全局变量和局部变量
'''
def test1():
    a = 300
    print("before:a= %d"%a)
    a = 100
    print("after:a= %d"%a)

def test2():
    a = 500
    print("test2：a= %d" % a)

test1()
test2()
'''

'''
a = 100

def test1():
    print("test1：a= %d" % a)
    
def test2():
    print("test2：a= %d" % a)
    
test1()
test2()
'''

#全局变量和局部变量名字相同
'''
a = 100
def test1():
    a = 300
    print("before:a= %d"%a)
    a = 100
    print("after:a= %d"%a)

def test2():
    print("test2：a= %d" % a)#局部优先使用，默认使用局部变量

test1()
test2()
'''

#在函数中修改全局变量
'''
a = 100
def test1():
    global a
    print("before:a= %d"%a)
    a = 333
    print("after:a= %d"%a)

def test2():
    print("test2：a= %d" % a)#局部优先使用，默认使用局部变量

test1()
test2()
'''