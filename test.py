from collections import deque

arr = []
arr = deque(arr)

arr.append('a')
arr.append('b')
arr.append('c')
arr.popleft()

print(arr)
