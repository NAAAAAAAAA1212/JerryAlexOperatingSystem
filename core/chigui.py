#init core
ver = "VERSION:1.0 GUI:TRUE LANG:CHINESE"
mail = "alexa@microsoft.zengqizhi.eu.org"
import time
import easygui
import random
import system32.auth
import system32.printf
import easygui
#kernel command
#boot password
try:
    while 2 == 2:
        while 1 == 1:
            usernm = easygui.enterbox(msg = "請輸入用戶名", title = "登入驗證程序")
            passwd = easygui.passwordbox(msg = "請輸入密碼", title = ("登入驗證程序 -- 登入為:", usernm))
            allow = system32.auth.authme(usernm, passwd, 0)
            if allow == 0:
                easygui.msgbox(msg = "對不起, 登入失敗!", title = "登入驗證程序", ok_button = "重試")
            if allow == 1:
                easygui.msgbox(msg = "登入成功", title = "登入驗證程序", ok_button = "繼續")
                break
            if allow == 2:
                easygui.msgbox(msg = "這個帳號已被禁止登入!", title = "登入驗證程序", ok_button = "重試")
    #dos system
        easygui.msgbox(msg = ("JAOS SYSTEM", ver, "ALL RIGHT RESERVED", "\nmail: ", mail, "\n你已登入為", usernm), title = "詳細資料", ok_button = "進入系統")
        while 1 == 1:
            command = easygui.buttonbox(msg = "DOS >>>\nver | 獲取版本資料\nmail | 獲取作者電郵\nwhoami | 我是誰\ntime | 獲得標準時間\nrandom | 獲取隨機數\nexit | 登出", title = "Jerry Alex Operating System", choices = ("ver", "mail", "whoami",  "time", "random", "exit"))
            if command == "ver":
                easygui.msgbox(msg = ver, title = "版本", ok_button = "繼續")
            if command == "mail":
                easygui.msgbox(msg = mail, title = "作者電郵", ok_button = "繼續")
            if command == "whoami":
                easygui.msgbox(msg = usernm, title = "我是誰", ok_button = "繼續")
            if command == "time":
                easygui.msgbox(msg = time.asctime( time.localtime(time.time()) ), title = "標準時間", ok_button = "繼續")
            if command == "random":
                rann1 = easygui.enterbox(msg = "MIN : ", title = "隨機數 : Min Number")
                rann2 = easygui.enterbox(msg = "MAX : ", title = "隨機數 : MAX Number")
                try:
                    easygui.msgbox(msg  = ("隨機數: ", random.randint(rann1, rann2)), title = "隨機數", ok_button = "繼續")
                except:
                    easygui.msgbox(msg = "對不起, 隨機數遇到了一點狀況!", title = "隨機數 : 錯誤", ok_button = "繼續")
            if command == "exit":
                break
    #logout
        while 1 == 1:
                ms = easygui.buttonbox(msg = "登入還是關機", title = "已登出", choices = ("登入", "關機"))
                out = 0
                if ms == "登入":
                    break
                if ms == "關機":
                    out = 1
                    break
        if out == 1:
            break
except:
    easygui.msgbox(msg = "對不起 JAOS 遇到了錯誤", title = "錯誤")
