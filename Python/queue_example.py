#Implementing Qeueu using list append() and pop()
qeueu = []
qeueu.append("a")
qeueu.append("b")
qeueu.append("c")

print(qeueu)

qeueu.pop()
qeueu.pop()
qeueu.pop()

print(qeueu)

#Implementing using deque (from collections)
from collections import deque
q = deque()

q.append(1)
q.append(2)
q.append(3)

print(q)

q.popleft()
q.popleft()
q.popleft()

print(q)

#Implementing using queue.Queue model
from queue import Queue
q = Queue(maxsize=3)
q.put(12)
q.put(122)
q.put(1234)

print(q)
print(q.full())

q.get()
print(q.full)
q.put(12)
print(q)
print(q.full())
print(q.qsize())