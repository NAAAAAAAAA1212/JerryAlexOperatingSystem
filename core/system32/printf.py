import time

def delay(text, delay = 0.2):
    for ch in text:
        print(ch, end = "", flush = True)
        time.sleep(delay)
    print()

def waiting(cycle, delay = 0.1):
    for i in range(cycle):
        for ch in ["-", "\\", "|", "/"]:
            print("\b%s"%ch, end = "", flush = True)
            time.sleep(0.1)
    print()

def cover(cycle, delay = 0.2):
    for i in range(cycle):
        s = "\r%d"%i
        print(s.ljust(3), end = "", flush = True)
        time.sleep(delay)
    print()