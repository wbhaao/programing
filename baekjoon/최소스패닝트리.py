import sys
import heapq
input = sys.stdin.readline
 
V, E = map(int, input().split())
# 방문 여부
visited = [False]*(V+1)
# 간선 저장
Elist = [[] for _ in range(V+1)]
# 현재그래프에서 짫은 경로 저장
heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])
 
answer = 0
cnt = 0
while heap:
    if cnt == V:
        break
    # 가중치, 노드
    w, s = heapq.heappop(heap)
    # 방문하지 않았다면
    if not visited[s]:
        visited[s] = True
        # 가중치 +
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)

print(answer)