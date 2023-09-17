from collections import deque

N = int(input())
M = int(input())
lst = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)
    lst[B].append(A)

q = deque()
q.append(1)
visited = [0] * (N+1)
visited[1] = 1

cnt = 0
while q:
    p = q.popleft()
    for i in lst[p]:
        if visited[i]==0:
            q.append(i)
            visited[i] = 1
            cnt += 1
print(cnt)