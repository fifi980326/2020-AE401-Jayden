# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:36:36 2020

@author: HARRY LIU
"""
#匯入模組
import random
#產生一個隨機數字
num=random.randint(1,10)
#輸入
a=input("請輸入數字")
#強制轉型
a=int(a)
#判斷
if a==num:
      print("答對")
else:
    print("答錯")
