# JAOS
## How to use?
Go to
```
./core/load.py
```
select your language
auth:
admin:admin
or
jaos:jaos
## Using Python Orgin File To Run
### Things That You Need In Order To Run
1. OS (OS-WIN for macOS and Windows, OS-SYS for Linux)
2. Tqdm
3. Easygui
### How to run?
Go to
```
./core/load.py
```
## Auth
### In order to set your own usernm and passwd
1. go to ./core/system32/auth.py
2. add the following codes into def authme():
```python
if usernm == "[your username]":
    if passwd == "[your password]":
        mode = 1
```

### In order to get sudo access
1. go to ./core/system32/auth.py
2. add the following codes into def authsudo():
```python
if usernm == "[your username (need to be same)]":
    mode = 1
        if passwd == "[your password (can be not the same)]":
            mode = 2
```
