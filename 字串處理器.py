# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:59:36 2020

@author: HARRY LIU
"""

import os.path #匯入os.path函式庫

content={}
####################

while True:
    
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    print("歡迎使用字串處理器")
    print("---------------------")
    print("功能：")
    print("1. 輸入檔案")
    print("2. 單字統計表")
    print("3. 查詢檔案中單字")
    print("4. 替換檔案中單字")
    print("5.離開系統 ")
    
    
    print("---------------------")
    function=input("請輸入要使用的功能選項：")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    
    
    if function == "1":
        fileName=input("請輸入檔案(含副檔名):")  
        if os.path.isfile(open):
            file=open(os.path,isfile)                
            content=file.read
            print("\n",content)
                        
        else:
                print("沒有此文件")
        file.close()
                    
    elif function == "2":
        if True:
            wordList=content.split
            print("文件共有",len,"個字")
        else:
            print("沒有內容 請先輸入檔案")
    
        
    
    elif function == "3":
        wordCount=0
        if content:
            searchWord=input("請輸入要搜尋的單字:")
            wordCount=
                    
    elif function == "4":

            
            else:            
                for k,v in d.items(): 
                    if ch == v:
                        print("英文：", k)
                        found=True
            if not found: 
                    print("此單字未在字典中喔！請重新輸入")
                    
    elif function == "5":
        score=0
        for k,v in d.items():
            print("中文：",v)
            ans=input("英文：")
            if ans == k:
                score = score + 1
                print("答對了！，目前分數是", score)
                print("-")
            else:
                print("答錯了！，目前分數是", score)
                print("-")
        print("測驗結束，你的分數是：", score)
    elif function == "6":
        break
    
    else:
        print("功能選項輸入錯誤！請重新輸入！")

