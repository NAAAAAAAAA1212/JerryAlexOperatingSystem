#init
boot = True
i1 = True
i2 = True

#testing
try:
    import os
except:
    i1 = False
try:
    import easygui
except:
    i2 = False

#output
if i1 == False:
    print("module OS not found, will not boot")
if i2 == False:
    print("module easygui not found, will not boot")
    boot = False

#boot
if boot == True:
    kernel = os.name
    if kernel == "nt":
        clear = "cls"
    if kernel == "posix":
        clear = "clear"
    os.system(clear)
    lang = "1"
    max = 1
    limit = 0
    num = 0
    print("1 = Up ; 2 = Down ; 3 = Enter")
    print("\033[1mLanguage: 語言: ")
    print("\033[1;30;47m1: English")
    print("\033[0m\033[1m2: 繁體中文")
    while 1 == 1:
        key = input()
        if key == "3":
            lang = str(num + 1)
            break
        if key == "1":
            num = num - 1
        if key == "2":
            num = num + 1
        if num < limit:
            num = limit
        if num > max:
            num = max
        os.system(clear)
        if num == 0:
            print("1 = Up ; 2 = Down ; 3 = Enter")
            print("\033[1mLanguage: 語言: ")
            print("\033[1;30;47m1: English")
            print("\033[0m\033[1m2: 繁體中文")
        if num == 1:
            print("1 = Up ; 2 = Down ; 3 = Enter")
            print("\033[1mLanguage: 語言: ")
            print("\033[0m\033[1m1: English")
            print("\033[1;30;47m2: 繁體中文\033[0m\033[1m")
    if lang == "1":
        if os.path.exists("core/eng.py") == True:
            os.system("python core/eng.py")
        else:
            print("lang file doesn't exsist! Please sel other lang!")
    if lang == "2":
        if os.path.exists("core/chi.py") == True:
            os.system("python core/chi.py")
        else:
            print("語言文件不存在! 請選擇其他語言!")
