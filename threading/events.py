import threading

event = threading.Event()

def action():
    print("Waiting for event trigger...\n")
    event.wait()
    print("Performing action XYZ now...\n")

t = threading.Thread(target=action)
t.start()

x = input("Do you want to trigger the event? (y/n)\n")

if x == "y":
    event.set()
