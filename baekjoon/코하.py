from collections import deque
import sys
read = sys.stdin.readline
M, N = map(int, read().split())

cnt = 0
graph = [[0] * (M + 1) for _ in range(M + 1)] 
visit_list2 = [0] * (M + 1)

for _ in range(N):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1
start, end = map(int, read().split())
q = deque()
q.append((start, 1))
visit_list2[start] = 1

result = -1
# queue를 통해 우선순위 정하면서
while q:
  # 현재 노드를 대기열에서 삭제
  vv, t = q.popleft()
  # 현재 노드 출력
  # 주변 노드 있으면 대기열에 저장 (작은순)
  for z in range(1, M+1):
    if graph[vv][z] == 1 and visit_list2[z]==0:
      if z == end:
          print(t)
          exit()
      q.append((z, t+1))
      visit_list2[z] = 1
print(result)