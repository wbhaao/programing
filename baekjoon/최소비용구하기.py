import heapq
from sys import maxsize
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

# 입력 받기
graph = [[] for _ in range(n + 1)]
visited = [maxsize] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

def dijkstra(x):
    # 간선 최소 비용 순으로 배열
    pq = []
    # (현재까지 비용, start)
    heapq.heappush(pq, (0, x))
    # 필요한 자원 : 0
    visited[x] = 0

    while pq:
        # 현재까지 비용, 현재 위치
        d, x = heapq.heappop(pq)
        # 현재까지 비용이 원래 비용보다 크다면
        if visited[x] < d:
            continue
        # 연결된 간선이 여러개 있을 수 있다.
        for nw, nx in graph[x]:
            # 간선을 연결 (이전모든노드와 다음 노드 비용합치기)
            nd = d + nw
            # 그 노드의 비용이 현재 비용보다 많다면 (교체)
            if visited[nx] > nd:
                # 합친 비용과 간 노드 위치 넣음
                heapq.heappush(pq, (nd, nx))
                # 최소비용 넣기
                visited[nx] = nd


dijkstra(start)

print(visited[end])