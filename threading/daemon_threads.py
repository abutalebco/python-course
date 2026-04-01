import threading
import time

path = "text.txt"
text = ""

def read_file():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def print_loop():
    for _ in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=read_file, daemon=True)
t2 = threading.Thread(target=print_loop)

t1.start()
t2.start()