import heapq
import sys

inpu = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a].append((cost, b))
    arr[b].append((cost, a))

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    total = [sys.maxsize] * (N+1)
    total[1] = 0
    while q:
        cost, node = heapq.heappop(q)
        if node == N:
            return total[node]
        if total[node] < cost:
            continue
        for ncost, nnode in arr[node]:
            if cost+ncost < total[nnode]:
                total[nnode] = cost+ncost
                heapq.heappush(q, (cost+ncost, nnode))

print(dijkstra())