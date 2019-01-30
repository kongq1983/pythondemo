
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

print(queue)

#'Eric'
queue.popleft()                 # The first to arrive now leaves
print(queue)

#John
queue.popleft()                 # The second to arrive now leaves

print(queue)