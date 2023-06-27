from collections import deque
n, m = map(int, input().split())
ground = []
for _ in range(n):
  ground.append(list(map(int, list(input()))))

def BFS():
  # n:4이고, m:6일떄
  '''
  [0, 0, 0, 0, 0, 0]
  [0, 0, 0, 0, 0, 0]
  [0, 0, 0, 0, 0, 0]
  [0, 0, 0, 0, 0, 0]
  '''
  visited = [[False]*m for _ in range(n)]
  # 3번째 : cnt
  q = deque()
  q.append((0, 0, 1))
  visited[0][0] = True
  while q:
    # 현재 i, j
    ci, cj, cnt = q.popleft()
    # print(v, end = " ")
    for i, j in ((1, 0), (0, 1), (0, -1), (-1, 0)):
      di, dj = ci+i, cj+j
      if (visited[di][dj]==False) and (ground[di][dj]==1)\
          and (di>=0) and (dj >= 0) and (di < n) and (dj < m):
        if (di==n and dj==m):
          return cnt+1
        
        q.append((di, dj, cnt+1))
        visited[di][dj] = True
print(BFS())