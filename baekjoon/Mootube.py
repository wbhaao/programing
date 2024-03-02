from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, usado = (map(int, input().split()))
    graph[a].append((b, usado))
    graph[b].append((a, usado))

for i in range(q):
    k, v = map(int, input().split())
    visited = [False] * (n + 1)
    visited[v] = True
    result = 0
    q = deque([(v, float('inf'))])

    while q:
        v, usado = q.pop()
        for next_v, next_usado in graph[v]:
            next_usado = min(usado, next_usado)
            if next_usado >= k and not visited[next_v]:
                result += 1
                q.append((next_v, next_usado))
                visited[next_v] = True
    print(result)