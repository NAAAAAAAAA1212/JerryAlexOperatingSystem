#init core
print("033[0;1m")
ver = "VERSION:1.0 GUI:FALSE LANG:CHINESE"
mail = "alexa@microsoft.zengqizhi.eu.org"
#startsys
#insert color
coldefault = "\033[0;1m"
colred = "\033[31;1m"
colgreen = "\033[32;1m"
colyellow = "\033[33;1m"
colblue = "\033[34;1m"
colpueple = "\033[35;1m"
colcyan = "\033[36;1m"
print(coldefault, "[", colgreen, "OK", coldefault, "] Color Output Data Online")
#start importing
import os
print(coldefault, "[", colgreen, "OK", coldefault, "] Kernel Command Online")
import time
print(coldefault, "[", colgreen, "OK", coldefault, "] Time Management System Online")
import easygui
print(coldefault, "[", colgreen, "OK", coldefault, "] PopUp System Online")
import random
import system32.auth
print(coldefault, "[", colgreen, "OK", coldefault, "] system32 Auth System Online")
import system32.printf
print(coldefault, "[", colgreen, "OK", coldefault, "] system32 Printf Output Online")
#kernel command
kernel = os.name
print(coldefault, "[", colgreen, "OK", coldefault, "] Kernel Info Get")
if kernel == "nt":
    clear = "cls"
if kernel == "posix":
    clear = "clear"
print(coldefault, "[", colgreen, "OK", coldefault, "] Clear Screen Command Get")
os.system(clear)
#boot password
while 2 == 2:
    while 1 == 1:
        print("請輸入密碼以登入!")
        usernm = input("帳戶: ")
        passwd = input("密碼 : ")
        allow = system32.auth.authme(usernm, passwd, 0)
        if allow == 0:
            print(colred, "帳戶或密碼錯誤!", coldefault)
        if allow == 1:
            print(colgreen, "登入成功!", coldefault)
            break
        if allow == 2:
            print(colyellow, "對不起!這個帳號已被禁止登入!", coldefault)
    os.system(clear)
#dos system
    print("JAOS SYSTEM", ver, "ALL RIGHT RESERVERD")
    print("作者電郵:", mail)
    print("如果不知道如何使用, 請輸入help!")
    print("你已登入為: ", usernm)
    while 1 == 1:
        command = input(("DOS", ver, usernm, ">>>"))
        status = 0
        if command == "help":
            print("ver          | 取得版本信息")
            print("mail         | 取得作者信息")
            print("whoami       | 你是誰")
            print("kernel       | 取得系統框架")
            print("clear        | 清空屏幕")
            print("time         | 取得標準時間")
            print("random       | 獲取隨機數")
            print("exit         | 關機")
            print("help         | 取得指令")
            print("sudo         | 執行管理員指令")
            print("python       | 進入python shell")
            if kernel == "nt":
                print("cmdstat      | 進入 cmd")
                print("cmd          | 執行 cmd 指令")
            if kernel == "posix":
                print("terminalstat | 進入 zsh")
                print("terminal     | 執行 terminal 指令")
            status = 1
        if command == "ver":
            print(ver)
            status = 1
        if command == "mail":
            print(mail)
            status = 1
        if command == "whoami":
            print(usernm)
            status = 1
        if command == "kernel":
            print(kernel)
        if command == "clear":
            os.system(clear)
            status = 1
        if command == "time":
            print(time.asctime( time.localtime(time.time()) ))
            status = 1
        if command == "random":
            rann1 = int(input("min: "))
            rann2 = int(input("max: "))
            try:
                print("num: ", random.randint(rann1, rann2))
            except:
                print(colred, "對不起!系統發現了錯誤!", coldefault)
            status = 1
        if command == "exit":
            status = 1
            break
        if command == "sudo":
            passwd = input("如果你要繼續, 請輸入密碼! >>> ")
            sudo = 0
            sudo = system32.auth.authsudo(usernm, passwd)
            if sudo == 2:
                sustatus = 0
                print("指令清單:")
                print("whoami | 你是誰")
                sucommand = input("你想要執行哪個指令? >>> ")
                if sucommand == "whoami":
                    print(colcyan, "ROOT", coldefault)
                    sustatus = 1
                if sustatus == 0:
                    print(colyellow, "對不起, 這個管理員指令不存在!", coldefault)
            if sudo == 1:
                print(colyellow, "對不起! 密碼錯誤!", coldefault)
            if sudo == 0:
                print(colyellow, "請詢問你的管理員以取得管理員權限!", coldefault)
            status = 1
        if command == "python":
            os.system("python")
            status = 1
        if command == "cmdstat":
            if kernel == "nt":
                while 3 == 3:
                    con = input("CMD >>> ")
                    if con == "exit":
                        break
                    else:
                        os.system(con)
                status = 1
        if command == "cmd":
            if kernel == "nt":
                con = input("CMD COMMAND >>> ")
                os.system(con)
                status = 1
        if command == "terminalstat":
            if kernel == "posix":
                while 3 == 3:
                    con = input("TERMINAL >>> ")
                    if con == "exit":
                        break
                    else:
                        os.system(con)
                status = 1
        if command == "terminal":
            if kernel == "posix":
                con = input("TERMINAL COMMAND >>> ")
                os.system(con)
                status = 1
        if status == 1:
            print(colgreen, "指令執行成功!", coldefault)
        if status == 0:
            print(colred, "這個指令 : \'", command, "\' 不是一個正確的指令, 如果需要幫助, 請輸入 \' help\'", coldefault)
    os.system("clear")
#logout
    print(colgreen, "登出狀態", coldefault)
    print(colpueple, "1.登入 還是 2.關機 ?", coldefault)
    while 1 == 1:
        ms = input()
        mss = 0
        out = 0
        if ms == "1":
            mss = 1
            break
        if ms == "2":
            mss = 1
            out = 1
            break
        if mss == 0:
            print(colred, "1 還是 2 !", coldefault)
    os.system(clear)
    if out == 1:
        break
    