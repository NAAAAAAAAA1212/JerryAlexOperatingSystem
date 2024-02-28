run = True

try:
    print("PACAGE NAME: clock.jaos")
    print("PUBLISHER: Offical JAOS")
    print("VERSION: 1.0")
    print("VERIFIED: TRUE")
    print("REQUIREMENTS: os, time")
    ask = input("Wish to run? [y] / [n]")
    if ask == "n":
        run = False
except:
    print("ERROR OCURED! APP WILL NOT INIT!")
    run = False
try:
    if (run):
        import os
        import time
except:
    print("ERROR OCURED! APP WILL NOT INIT!")
    run = False

if (run):
    try:
        kernel = os.name
        if kernel == "nt":
            clear = "cls"
        if kernel == "posix":
            clear = "clear"
    except:
        print("ERROR OCURED! APP FAILED INIT!")
        run = False

if (run):
    try:
        os.system(clear)
        while(True):
            print("PRESS [CTRL + C] TO EXIT")
            print("TIME:", time.asctime( time.localtime(time.time())))
            try:
                time.sleep(1)
            except:
                print("[CTRL + C] HAS BEEN TRIGRED! EXITED WITH CODE 0")
                break
            os.system(clear)
    except:
        print("ERROR OCURED! APP FAILED ON RUNTIME!")