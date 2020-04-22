# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:25:02 2020

@author: HARRY LIU
"""


#匯入模組
import random
#產生一個隨機數字
num=random.randint(1,20)
#輸入
a=input("請輸入數字:")
#強制轉型
a=int(a)
#判斷
if a<num:
    print("太小")
elif a>num:
    print("太大")
elif a==num:
      print("答對")
while i<5:
    print("輸")
    while i<4:
        print("贏")