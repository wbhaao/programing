'''
분리 집합을 사용하여 풀어야 한다

선플레이어가 홀수번째
후플레이어가 짝수번째

원점으로 돌아오는 검사해야함 -> bfs

'''
from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    q = deque(graph[A])
    while q:
        v = q.popleft()
        for i in graph[v]:
            q.append(i)
            if i==B:
                print(i+1)
                exit()
print(0)