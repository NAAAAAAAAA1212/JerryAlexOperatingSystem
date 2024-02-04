import os
kernel = os.name
if kernel == "nt":
    clear = "cls"
if kernel == "posix":
    clear = "clear"
os.system(clear)
print("JAOS Boot Loader")
print("Scanning for bootable files......")
os.system(clear)
print("JAOS Boot Loader")
print("Bootable files found!")
print(".py bootable file:")
for file in os.listdir("./core"):
    if file.endswith(".py"):
        print(os.path.join(file))
print(".jar bootable file:")
for file in os.listdir("./core"):
    if file.endswith(".jar"):
        print(os.path.join(file))
bootwhat = input("Please Select which one you want to boot:")
lang = "exit"
if bootwhat.endswith(".py"):
    lang = "python3 ./core/" + bootwhat
if bootwhat.endswith(".jar"):
    lang = "java -jar ./core/" + bootwhat
os.system(lang)
os.system(clear)