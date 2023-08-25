# dequeue (Doubly Ended Queue) : append and pop operations from both the ends
# deque provides an O(1) time complexity for append and pop
from collections import deque


queue1: deque = deque()
queue1.append(3)
queue1.append(5)
queue1.append(8)
print(queue1)

queue1.popleft()
queue1.pop()
print(queue1)
