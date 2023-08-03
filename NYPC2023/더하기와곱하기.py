from collections import deque
import sys

read = sys.stdin.readline

N = int(read())
M = read()

queue = deque()
queue.append((M, 0))

while queue:
    v, i = queue.popleft()
    if int(M) == 0:
        print(i+1)
        exit()
    if M[-1]=='0':
        queue.append(((M[:-1]+'1')[-N:], i+1))
    else:
        queue.append(((M[:-1]+'0')[-N:], i+1))
    queue.append(((M[:-1]+'0')[-N:], i+1))