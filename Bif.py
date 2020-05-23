# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:57:08 2020

@author: HARRY LIU
"""


scores=[]

num=input("請輸入人數:")
num=int(num)
for i in range(num): 
   x=input("輸入分數:") 
   x=int(x)
   scores.append(x)
print(scores)
######
a =max(scores)
b =min(scores)
c =sum(scores)/num
print("最高",a)
print("最低",b)
print("平均",c)






