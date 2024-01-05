#init
gui = True
boot = True
i1 = True
i2 = True
out = 0

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
    boot = False
if i2 == False:
    print("module easygui not found, GUI will be disabled")
    gui = False

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
    print("\033[0m\033[1m1 = Up ; 2 = Down ; 3 = Enter\033[0m\033[1m")
    print("\033[0m\033[1mLanguage: 語言: \033[0m\033[1m")
    print("\033[0m\033[1;30;47m1: English\033[0m\033[1m")
    print("\033[0m\033[1m2: 繁體中文\033[0m\033[1m")
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
            print("\033[0m\033[1m1 = Up ; 2 = Down ; 3 = Enter\033[0m\033[1m")
            print("\033[0m\033[1mLanguage: 語言: \033[0m\033[1m")
            print("\033[0m\033[1;30;47m1: English\033[0m\033[1m")
            print("\033[0m\033[1m2: 繁體中文\033[0m\033[1m")
        if num == 1:
            print("\033[0m\033[1m1 = Up ; 2 = Down ; 3 = Enter\033[0m\033[1m")
            print("\033[0m\033[1mLanguage: 語言: \033[0m\033[1m")
            print("\033[0m\033[1m1: English\033[0m\033[1m")
            print("\033[0m\033[1;30;47m2: 繁體中文\033[0m\033[1m")
    os.system(clear)
    if gui == True:
        print("\033[0m\033[1m1 = Up ; 2 = Down ; 3 = Enter\033[0m\033[1m")
        print("\033[0m\033[1mGUI:\033[0m\033[1m")
        print("\033[0m\033[1;30;47m1: DOS\033[0m\033[1m")
        print("\033[0m\033[1m2: Run On Dos with popup\033[0m\033[1m")
        print("\033[0m\033[1m3: GUI\033[0m\033[1m")
        lang = "1"
        max = 2
        limit = 0
        num = 0
        while 1 == 1:
            key = input()
            if key == "3":
                out = str(num)
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
                print("\033[0m\033[1m1 = Up ; 2 = Down ; 3 = Enter\033[0m\033[1m")
                print("\033[0m\033[1mGUI:\033[0m\033[1m")
                print("\033[0m\033[1;30;47m1: DOS\033[0m\033[1m")
                print("\033[0m\033[1m2: Run On Dos with popup\033[0m\033[1m")
                print("\033[0m\033[1m3: GUI\033[0m\033[1m")
            if num == 1:
                print("\033[0m\033[1m1 = Up ; 2 = Down ; 3 = Enter\033[0m\033[1m")
                print("\033[0m\033[1mGUI:\033[0m\033[1m")
                print("\033[0m\033[1m1: DOS\033[0m\033[1m")
                print("\033[0m\033[1;30;47m2: Run On Dos with popup\033[0m\033[1m")
                print("\033[0m\033[1m3: GUI\033[0m\033[1m")
            if num == 2:
                print("\033[0m\033[1m1 = Up ; 2 = Down ; 3 = Enter\033[0m\033[1m")
                print("\033[0m\033[1mGUI:\033[0m\033[1m")
                print("\033[0m\033[1m1: DOS\033[0m\033[1m")
                print("\033[0m\033[1m2: Run On Dos with popup\033[0m\033[1m")
                print("\033[0m\033[1;30;47m3: GUI\033[0m\033[1m")
    os.system(clear)
    if lang == "1" and out == "0":
        if os.path.exists("core/eng.py") == True:
            os.system("python core/eng.py")
        else:
            print("File doesn't exsist!")
    if lang == "2" and out == "0":
        if os.path.exists("core/chi.py") == True:
            os.system("python core/chi.py")
        else:
            print("文件不存在!")
    if lang == "1" and out == "1":
        if os.path.exists("core/engg1.py") == True:
            os.system("python core/engg1.py")
        else:
            print("File doesn't exsist!")
    if lang == "2" and out == "1":
        if os.path.exists("core/chig1.py") == True:
            os.system("python core/chig1.py")
        else:
            print("文件不存在!")
    if lang == "1" and out == "2":
        if os.path.exists("core/engg2.py") == True:
            os.system("python core/engg2.py")
        else:
            print("File doesn't exsist!")
    if lang == "2" and out == "2":
        if os.path.exists("core/chig2.py") == True:
            os.system("python core/chig2.py")
        else:
            print("文件不存在!")