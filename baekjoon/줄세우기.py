import sys
from collections import deque
input = sys.stdin.readline
result = []
N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    lst[B].append(A)  
visited = [False] * (N+1)

q = deque()
for i in range(1, N+1):
        if (lst[i]==[]):
            q.append(i)
            visited[i] = True
while q:
    a = q.popleft()
    result.append(a)
    for i in range(1, N+1):
        try:
            lst[i].remove(a)
        except:
            pass
    for i in range(1, N+1):
        if (lst[i]==[]) and (not visited[i]):
            q.append(i)
            visited[i] = True
print(*result)