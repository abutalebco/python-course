import queue

q1 = queue.Queue()
q2 = queue.LifoQueue()
q3 = queue.PriorityQueue()

objects = [(1, "Mohamed"), (9, "Hossam"), (3, "Jamal"), (11, "Mohsen"), (5, "Sadeq")]

for object in objects:
    q1.put(object)
    q2.put(object)
    q3.put(object)

print(" -------- QUEUE -------- ")
print(q1.get()[1]) # Mohamed printed as it is written above
print(q1.get()[1])
print(q1.get()[1])
print(q1.get()[1])
print(q1.get()[1])

print(" -------- LIFO QUEUE -------- ")
print(q2.get()[1])
print(q2.get()[1])
print(q2.get()[1])
print(q2.get()[1])
print(q2.get()[1])

print(" -------- PRIORITY QUEUE -------- ")
print(q3.get()[1])
print(q3.get()[1])
print(q3.get()[1])
print(q3.get()[1])
print(q3.get()[1])