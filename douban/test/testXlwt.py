# -*- codeing = utf-8 -*-
# @time : 2021.9.12 22:28
# @Author: dltu
# @File : testXlwt.py
# @Software: PyCharm



import xlwt
'''
workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表
worksheet.write(0,0,'hello')    #写入数据，行，列，参数内容
workbook.save("student.xls")    #保存数据表
'''

workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表

for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(j+1,i+1,(i+1)*(j+1)))
print("输入完成")


workbook.save("student.xls")    #保存数据表



