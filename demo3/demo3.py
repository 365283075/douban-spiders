# -*- codeing = utf-8 -*-
# @time : 2021.9.7 15:17
# @Author: dltu
# @File : demo3.py
# @Software: PyCharm


'''
print("test-----------1")

f = open("123.txt", "r") #用只读模式打开了一个不存在的文件，报错

print("test-----------2")#这句代码不会被执行

#捕获异常
try:
    print("test-----------1")

    f = open("123.txt","r")

    print("test-----------2")

except IOError:  #文件没找到，属于IO异常（输入输出异常）
    pass         #捕获异常后，执行的代码
'''

'''
try:
    print(num)
# except IOError:
except NameError:
    print("产生错误")
'''

'''
try:
    print("test-----------1")

    f = open("123.txt", "r")  # 用只读模式打开了一个不存在的文件，报错

    print("test-----------2")  # 这句代码不会被执行

    print(num)

except(NameError,IOError):  #将所有可能产生的异常都放到下面的小括号里
    print("产生错误")
'''

'''
try:
    print("test-----------1")

    f = open("test.txt", "r")  # 用只读模式打开了一个不存在的文件，报错

    print("test-----------2")  # 这句代码不会被执行

    print(num)

except(NameError,IOError) as result:  #将所有可能产生的异常都放到下面的小括号里
    print("产生错误")
    print(result)
'''

'''
try:
    print("test-----------1")

    f = open("123.txt", "r")  # 用只读模式打开了一个不存在的文件，报错

    print("test-----------2")  # 这句代码不会被执行

    print(num)

except Exception as result:  #将所有可能产生的异常都放到下面的小括号里
    print("产生错误")
    print(result)
'''

#try...finally 和嵌套
'''
import time
try:
    f = open("test.txt","r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("发生异常...")
'''


#作业

f = open("gushi.txt","w")

f.write('''床前明月光，
疑似地上霜。
举头望明月，
低头思故乡。''')

def read():

    f = open("gushi.txt", "r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            print(content)
    finally:
        f.close()

def write():
    f = open("copy.txt", "w")

    f.write(read())

    print("复制完毕")

write()