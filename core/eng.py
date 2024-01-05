#init core
print("033[0;1m")
ver = "VERSION:0.1"
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
print(coldefault, "[", colgreen, "OK", coldefault, "] Random System Online")
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
        print("To enter JAOS, please insert your credential!")
        usernm = input("usernm : ")
        passwd = input("passwd : ")
        allow = system32.auth.authme(usernm, passwd, 0)
        if allow == 0:
            print(colred, "Sorry! Wrong Credential!", coldefault)
        if allow == 1:
            print(colgreen, "LOGIN SUCCESS", coldefault)
            break
        if allow == 2:
            print(colyellow, "Sorry! The account you are trying to login is not reachable!", coldefault)
    os.system(clear)
#dos system
    print("JAOS SYSTEM", ver, "ALL RIGHT RESERVERD")
    print("mail:", mail)
    print("To get all the commands, type help")
    print("You have logged in as", usernm)
    while 1 == 1:
        command = input(("DOS", ver, usernm, ">>>"))
        status = 0
        if command == "help":
            print("ver          | getting the version")
            print("mail         | geting the author's mail")
            print("whoami       | who you are")
            print("kernel       | getting the system kernel")
            print("clear        | clearing the screen")
            print("time         | getting the std time")
            print("random       | getting a random number")
            print("exit         | shutdown the system")
            print("help         | getting support of command")
            print("sudo         | get root")
            print("python       | get python shell")
            if kernel == "nt":
                print("cmdstat      | run in cmd")
                print("cmd          | run cmd command")
            if kernel == "posix":
                print("terminalstat | run in zsh")
                print("terminal     | run terminal command")
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
                print(colred, "Sorry! the number you typed will make the os broken!", coldefault)
            status = 1
        if command == "exit":
            status = 1
            break
        if command == "sudo":
            passwd = input("To continue, please input your password! >>> ")
            sudo = 0
            sudo = system32.auth.authsudo(usernm, passwd)
            if sudo == 2:
                sustatus = 0
                print("Command List:")
                print("whoami | who you are")
                sucommand = input("Which command you want to execute? >>> ")
                if sucommand == "whoami":
                    print(colcyan, "ROOT", coldefault)
                    sustatus = 1
                if sustatus == 0:
                    print(colyellow, "Sorry, but this sudo command doesn't exist!", coldefault)
            if sudo == 1:
                print(colyellow, "Sorry! Wrong Password!", coldefault)
            if sudo == 0:
                print(colyellow, "Please ask your administrator for sudo access!", coldefault)
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
            print(colgreen, "Command Exectued!", coldefault)
        if status == 0:
            print(colred, "The command you typed, which is : \'", command, "\'is not a valid command, if you have any problems, please type \' help\'", coldefault)
    os.system("clear")
#logout
    print(colgreen, "LOGGED OUT", coldefault)
    print(colpueple, "Login or Shutdown ?", coldefault)
    while 1 == 1:
        ms = input()
        mss = 0
        out = 0
        if ms == "login":
            mss = 1
            break
        if ms == "shutdown":
            mss = 1
            out = 1
            break
        if mss == 0:
            print(colred, "PLEASE CHOOSE ONE OF THESE!", coldefault)
    os.system(clear)
    if out == 1:
        break
    