# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:59:36 2020

@author: HARRY LIU
"""

import os.path #匯入os.path函式庫

content=""
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
            file=open(fileName,"r")                
            content=file.read()
            print("\n",content)
                        
        else:
                print("沒有此文件")
        file.close()
                    
    elif function == "2":
        if content:
            wordList=content.split()
            print("文件共有",len(wordList),"個字")
        else:
            print("沒有內容 請先輸入檔案")
    
    elif function=="3":            
        wordCount=0#單字計數預設為0
        
        if content:   #如果有內容變數(True)，表示有讀取到內容
            searchWord=input("請輸入要搜尋的單字：")#輸入搜尋單字(input)
            wordCount=content.count(searchWord)#計算字串中單字數量(count)
            print(searchWord,"共出現了",wordCount,"次") #印出單字共出現了幾次(print)
            
        else:
            print("沒有內容！請先輸入檔案！")
                    
    elif function == "4":
                 
        if content:   #如果有內容變數(True)，表示有讀取到內容
            oldWord=input("請輸入要替換的單字：")#輸入要替換的單字
            newWord=input("請輸入新的單字：")#輸入新的單字
            content=content.replace(oldWord,newWord)#用字串取代(replace)
            print("更新後內容：\n",content )
            file=open(fileName,"w")#打開文件,寫入模式
            file.write(content)#更新寫入新字串
            file.close()#關閉文件
        else:
            print("沒有內容！請先輸入檔案！")


