from collections import deque
import sys
read = sys.stdin.readline

n, m, v = map(int, read().split())
cnt = 0
graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = deque([0] * (n + 1))
visit_list2 = [0] * (n + 1)

# 간선 연결하기
# 순서상관 없게 하기 위해서 ab ba 둘다 함
for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

# 재귀를 통해 깊이우선탐색
def dfs(root):
  visit_list[root] = 1
  # 현재 노드 출력
  print(root, end=" ")
  # 주위 노드 있다면 바로 함수실행
  for i in range(1, n+1):
    if graph[root][i] == 1 and visit_list[i]==0:
      dfs(i)
    
dfs(v)
print()
q = deque()
q.append(v)
visit_list2[v] = 1
# queue를 통해 우선순위 정하면서
while q:
  # 현재 노드를 대기열에서 삭제
  vv = q.popleft()
  # 현재 노드 출력
  print(vv, end=" ")
  # 주변 노드 있으면 대기열에 저장 (작은순)
  for z in range(1, n+1):
    if graph[vv][z] == 1 and visit_list2[z]==0:
      q.append(z)
      visit_list2[z] = 1
## visit_list2를 if 안에 넣지 않으면 같은 값이 2개이상 들어갈 수 있다.