# -*- codeing = utf-8 -*-
# @time : 21.8.31 16:57
# @Author: dltu
# @File : demo4.py
# @Software: PyCharm

'''
for i in range(5):
    print(i)
'''

'''
for i in range(0,11,3):  #从0开始到11介绍，步进值为3（每次+3）
    print(i)
'''
'''
for i in range(-10,-100,-30):
    print(i)
'''

'''
name = "chengdu"
for x in name:
    print(x,end="\t")
'''

'''
a = ["aa","bb","cc","dd"]
print(len(a))
for i in range(len(a)):
    print(i,a[i])
'''

'''
i = 0
while i < 5 :
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%1)
    i += 1
'''

#1-100求和
'''
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1-%d 的和为：%d"%(n,sum))

sum = 0
for i in range(1,101):

    sum += i

print(sum)


count = 10
while count<5:
    print(count,"小于5")
    count += 1
else:
    print(count,"大于或等于5")


i = 0
while i <10:
    i = i+1
    print("-"*30)
    if i==5:
        break  #结束整个while循环
    print(i)
    

i = 0
while i <10:
    i = i+1
    print("-"*30)
    if i==5:
        continue #结束本次循环
    print(i)


#99乘法表
#x行 y列
for x in range(1,10):
    print("")
    for y in range(1,1+x):
        z = x * y
        print("%d*%d=%d\t"%(x,y,z),end="")

#错误的思路
a = 0
b = 0
c = a*b
for a in range(1,10):
    for b in range(1,a+1):
        print("%d*%d=%d\t"%(a,b,a*b),end="")
    print()
#一行代码
#print("%d*%d=%d\t"%(a,b,a*b),)--放弃
 '''




