import hashlib
import os

def authlogin(user = "", password = "") -> bool:
    if os.path.isfile("./login/user/" + user):
        with open("./login/user/" + user, "r") as keyfile:
            key = keyfile.read()
        if hashlib.sha256(password.encode('utf-8')).hexdigest() == key:
            return True
    return False

def changepassword(user = "", password = "") -> None:
    if os.path.exists("./login/user"):
        with open("./login/user/" + user, "w") as keyfile:
            keyfile.write(hashlib.sha256(password.encode('utf-8')).hexdigest())

def authsudo(user = "", password = "") -> bool:
    if os.path.isfile("./login/admin/" + user):
        with open("./login/admin/" + user, "r") as keyfile:
            key = keyfile.read()
        if hashlib.sha256(password.encode('utf-8')).hexdigest() == key:
            return True
    return False

def writesudo(user = "", password = "") -> None:
    if os.path.exists("./login/admin"):
        with open("./login/admin/" + user, "w") as keyfile:
            keyfile.write(hashlib.sha256(password.encode('utf-8')).hexdigest())

