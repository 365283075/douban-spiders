# -*- codeing = utf-8 -*-
# @time : 2021.9.7 10:16
# @Author: dltu
# @File : demo2.py
# @Software: PyCharm

#namelist = []  #定义一个空的列表

'''
namelist = ["小张","小王","小李"]

testlist = [1,"测试"]
print(type(testlist[0]))
print(type(testlist[1]))

print(namelist[0])
print(namelist[1])
print(namelist[2])



namelist = ["小张","小王","小李"]
for name in namelist:
    print(name)

print(len(namelist)) #得到列表的长度

length = len(namelist)

i = 0

while i<length:
    print(namelist[i])
    i += 1


namelist = ["小张","小王","小李"]
#增加： 【append】
print("---增加前---")
for name in namelist:
    print(name)

nametemp = input("请输入")
namelist.append(nametemp)

print("---增加后---")
for name in namelist:
    print(name)



a = [1,2]
b = [3.4]
a.append(b) #将列表当做一个元素加入到a列表
print(a)

a.extend(b) #将b列表中的每一个元素注意加入到a
print(a)

#增： 【insert】

a = [0,1,2]
a.insert(1,3)  #(下标，元素)
print(a)       #指定下标位置插入元素



#删： [del] [pop] [remove]
movieName = ["0","1","2","3","4","3"]
print("---删除前---")
for name in movieName:
    print(name)

#del movieName[2] #删除指定下标
#movieName.pop()  #弹出最后一个
movieName.remove("3")#指定名称

print("---删除后---")
for name in movieName:
    print(name)
'''


namelist = ["小张","小王","小李"]
'''
print("---修改前---")
for name in namelist:
    print(name)

namelist[1] = "小红"

print("---修改后---")
for name in namelist:
    print(name)
'''

#查 ： [in not in ]
'''
findName = input("请输入你要查找的学员名称")

if findName in namelist:
    print("找到了")
else：
    print("无")

'''

'''
mylist = ["a","b","c","a","b"]

print(a.index("a",1,4)) #查指定下标范围的元素，并返回下标

print(a.index("a",1,3)) #左闭右开 [1,3）



print(mylist.count("c")) #统计次数

'''
'''

a = [1,4,2,3]
print(a)
a.reverse()#将列表所有元素反转
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)
'''

'''
#schoolNames = [[],[],[]] #有三个元素的空列表，每个元素都是空列表

schoolNames = [[1,2],[3,4,5],[6,7]]
print(schoolNames[0][1])
'''

import random

offices = [[],[],[]]

names = ["A","B","C","D","E","F","G","H"]

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数：%d"%(i,len(office)))
    i += 1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)









