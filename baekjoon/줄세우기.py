import sys
from collections import deque
input = sys.stdin.readline
result = []
N, M = map(int, input().split())

visited = [False] * (N+1)
lst = [[] for _ in range(N+1)]

indegree = [0] * (N+1)
for i in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)  
    indegree[B] += 1
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    result.append(now)
    for i in lst[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
print(*result)