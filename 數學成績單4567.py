# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:16:26 2020

@author: HARRY LIU
"""
math=list()
num=input("全班人數:")
num=int(num)
for i in range(num):
    name=input("學生姓名:")
    scores=input("數學成績:")
    scores=int(scores)
    
    
    student=list()
    student.append(name)
    student.append(scores)
    
    math.append(student)
    
    
print("數學成績單:",math)

sum=0

for i in math:
    sum=sum+i[1]
    
    
Avg=sum/num
print("平均分數=",Avg)




highest=0

for i in math:
    if i[1]>highest:
       highest=i[1]
       higheststudent=i[0]
print("最高分是",higheststudent,highest,"分")

lowest=100
for i in math:
    if i[1]<lowest:
        lowest=i[1]
        loweststudent=i[0]
print("最低分是",loweststudent,lowest,"分")








