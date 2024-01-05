#init core
ver = "VERSION:1.0 GUI:TRUE LANG:ENGLISH"
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
            usernm = easygui.enterbox(msg = "Please Insert Your Username", title = "Auth")
            passwd = easygui.passwordbox(msg = "Please Insert Your Password", title = ("Auth -- Login as:", usernm))
            allow = system32.auth.authme(usernm, passwd, 0)
            if allow == 0:
                easygui.msgbox(msg = "Sorry, login failed!", title = "Auth", ok_button = "retry")
            if allow == 1:
                easygui.msgbox(msg = "Login Succes", title = "Auth", ok_button = "continue")
                break
            if allow == 2:
                easygui.msgbox(msg = "This account is not allowed to login!", title = "Auth", ok_button = "retry")
    #dos system
        easygui.msgbox(msg = ("JAOS SYSTEM", ver, "ALL RIGHT RESERVED", "\nmail: ", mail, "\nYou have logged in as", usernm), title = "details", ok_button = "enter dos")
        while 1 == 1:
            command = easygui.buttonbox(msg = "DOS >>>\nver | getting version\nmail | getting mail\nwhoami | who r u\ntime | getting standard time\nrandom | getting random number\nexit | exit", title = "Jerry Alex Operating System", choices = ("ver", "mail", "whoami",  "time", "random", "exit"))
            if command == "ver":
                easygui.msgbox(msg = ver, title = "ver", ok_button = "got it")
            if command == "mail":
                easygui.msgbox(msg = mail, title = "mail", ok_button = "got it")
            if command == "whoami":
                easygui.msgbox(msg = usernm, title = "whoami", ok_button = "got it")
            if command == "time":
                easygui.msgbox(msg = time.asctime( time.localtime(time.time()) ), title = "time", ok_button = "got it")
            if command == "random":
                rann1 = easygui.enterbox(msg = "MIN : ", title = "random : Min Number")
                rann2 = easygui.enterbox(msg = "MAX : ", title = "random : MAX Number")
                try:
                    easygui.msgbox(msg  = ("num: ", random.randint(int(rann1), int(rann2))), title = "random", ok_button = "Got it")
                except:
                    easygui.msgbox(msg = "Sorry, but random occurred an error!", title = "random : error", ok_button = "Got it")
            if command == "exit":
                break
    #logout
        while 1 == 1:
            ms = easygui.buttonbox(msg = "Login or Shutdown ?", title = "LOGGED OUT", choices = ("login", "shutdown"))
            out = 0
            if ms == "login":
                break
            if ms == "shutdown":
                out = 1
                break
        if out == 1:
            break
except:
    easygui.msgbox(msg = "Sorry JAOS occureed an arror", title = "ERROR")
