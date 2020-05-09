# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:22:07 2020""

@author: HARRY LIU
"""
scores=[]
studername=[]
num=input("請輸入人數:")
num=int(num)
for i in range(num):
    name=input("學生姓名")
    studername.append(name)
    x=input("輸入分數:")
    x=int(x)
    scores.append(x)
print(scores)
######
sum=0
for i in range(num):
    sum = sum + scores [i]
avg = sum/num
print("平均分數:",avg)
###
highest=0
lowest=100
for i in range(num):
    if scores[i]>highest:
        highest=scores[i]
        h=i
    if scores[i]<lowest:
        lowest=scores[i]
        l=i
print("最高分",highest,"是",studername[h])
print("最低分",lowest,"是",studername[l])



