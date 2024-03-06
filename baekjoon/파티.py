import heapq

def dijkstra(s):
    D = [float('inf')] * (N+1)
    D[s] = 0
    q = []								    # 최단 거리 테이블을 heap으로 구현
    heapq.heappush(q, (0, s))				# heap에 (가중치, 노드) 형식으로 삽입 
    while q:
        dist, now = heapq.heappop(q)		# 최소힙이므로 가중치가 가장 작은 값이 pop
        if D[now] >= dist:					# 이미 최솟값 구했는지 확인
            for v, val in city[now]:		# 연결된 노드들 확인
                if dist + val < D[v]:		# 가중치가 더 작은 값이면 갱신
                    D[v] = dist + val
                    heapq.heappush(q, (dist + val, v))
    return D

N, M, X = map(int, input().split())
city = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    city[a].append([b, t])
ans = dijkstra(X)
ans[0] = 0
for i in range(1, N+1):
    if i != X:
        res = dijkstra(i)
        ans[i] += res[X]

print(max(ans))