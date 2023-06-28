'''
이제 BFS가 진짜 쉬워졌다.
'''
from collections import deque
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline
'''
N : 도시의 개수
M : 도로의 개수
K : 거리 정보
X : 출발 도시의 번호
'''
N, M, K, X = map(int, input().split())
visited = [0]*N
graph = [[] for _ in range(N)]
for i in range(M):
  # 오퍼레이터, 오퍼랜드 : 그냥 연산자, 피연산자 뜻, 
  oprt, oprd = map(int, input().split())
  graph[oprt-1].append(oprd-1)

def BFS():
  q = deque()
  q.append((X-1, 1))
  result = []
  while q:
    curNode, time = q.popleft()
    for i in graph[curNode]:
      if visited[i] == 0:
        if time==K:
          result.append(i+1)
        elif time>K:
          break
        else:
          visited[i] = 1
          q.append((i, time+1))
  return result
bfs = BFS()
if not bfs:
  print(-1)
else:
  for i in bfs:
    print(i)