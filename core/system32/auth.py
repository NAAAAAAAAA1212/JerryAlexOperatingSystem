def authme(usernm, passwd, outputmode):
    mode = 0
    if usernm == "admin":
        if passwd == "admin":
             mode = 1
    if usernm == "alexa":
        if passwd == "creator":
             mode = 1
    if usernm == "jaos":
        if passwd == "jaos":
             mode = 1
    if usernm == "root":
        if passwd == "":
             mode = 2
    if usernm == "defaultuser0":
        if passwd == "defaultuser0":
             mode = 2
    if outputmode == 1:
        if mode == 2:
            mode = 0
    return mode
def authsudo(usernm, passwd):
    mode = 0
    if usernm == "admin":
        mode = 1
        if passwd == "admin":
             mode = 2
    if usernm == "alexa":
        mode = 1
        if passwd == "creator":
             mode = 2
    if usernm == "sudo":
        mode = 1
        if passwd == "":
            mode = 2
    if usernm == "defaultuser0":
        mode = 1
        if passwd == "defaultuser0":
            mode = 2
    return mode