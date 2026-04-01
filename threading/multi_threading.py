import threading

def greeting():
    for _ in range(5):
        print("Hello, World!")

def name():
    for _ in range(5):
        print("Mohamed")

t1 = threading.Thread(target=greeting)
t2 = threading.Thread(target=name)

t1.start()
t2.start()