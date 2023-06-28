'''
이제 BFS가 진짜 쉬워졌다.
'''
from collections import deque
import sys
read = sys.stdin.readline
'''
N : 도시의 개수
M : 도로의 개수
K : 거리 정보
X : 출발 도시의 번호
'''
N, M, K, X = map(int, read().split())
visited = [0]*N
distance = [0]*N
graph = [[] for _ in range(N)]
for _ in range(M):
  # 오퍼레이터, 오퍼랜드 : 그냥 연산자, 피연산자 뜻, 
  oprt, oprd = map(int, read().split())
  graph[oprt-1].append(oprd-1)

def BFS():
  result = []
  q = deque()
  q.append(X-1)
  visited[X-1] = 1
  distance[X-1] = 0
  while q:
    curNode = q.popleft()
    for i in graph[curNode]:
      if visited[i] == 0:
          visited[i] = 1
          q.append(i)
          distance[i] = distance[curNode] + 1
          if distance==K:
            result.append(i)
  if not result:
    print(-1)
  else:
    result.sort()
    for j in result:
      print(j, end='\n')
BFS()
