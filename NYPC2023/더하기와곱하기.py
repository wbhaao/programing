from collections import deque
import sys

read = sys.stdin.readline

N = int(read())
M = read()

temp = 2 ** (N)
value = int(M, 2)

queue = deque()
queue.append((value, 0))

while queue:
    v, i = queue.popleft()
    if (v*2)%(2**N)==0 or (v+1)%(2**N)==0:
        print(i+1)
        exit()
    queue.append(((v*2)%(temp), i+1))
    queue.append(((v+1)%(temp), i+1))