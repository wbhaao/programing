from collections import deque
import sys

read = sys.stdin.readline
N, M, K, X = map(int, read().split())
visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
  # 오퍼레이터, 오퍼랜드 : 그냥 연산자, 피연산자 뜻, 
  oprt, oprd = map(int, read().split())
  graph[oprt].append(oprd)

def BFS():
  result = []
  q = deque()
  q.append((X, 1))
  visited[X] = 1
  while q:
    curNode, time = q.popleft()
    for i in graph[curNode]:
      if visited[i] == 0:
        q.append((i, time+1))
        # 정답이면 visited를 1로 안했었는데
        # 정답이라도 들어갔다 해야한다
        # https://uncovered-grain-c53.notion.site/cecfd5b39701414f899de5abb6148441?pvs=4
        # 이해돕기
        visited[i] = 1
        if time==K:
          result.append(i)
        elif time>K:
          break
        
  return result
bfs = BFS()
if not bfs:
  print(-1)
else:
  bfs.sort()
  for i in bfs:
    print(i)