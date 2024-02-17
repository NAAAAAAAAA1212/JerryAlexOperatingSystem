import time

def waiting(cycle, delay = 0.1):
    for i in range(cycle):
        for ch in ["-", "\\", "|", "/"]:
            print("\b%s"%ch, end = "", flush = True)
            time.sleep(delay)

while(True):
    waiting(1)