from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # deque([1, 2, 3])
stack.pop()  # 3
stack.pop()  # 2
stack.pop()  # 1
print(stack)  # deque([])
stack.pop()  # IndexError: pop from an empty deque




queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])
queue.popleft()  # 1
queue.popleft()  # 2
queue.popleft()  # 3
print(queue)  # deque([])
queue.popleft()  # IndexError: pop from an empty deque