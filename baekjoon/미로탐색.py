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
  
  원래 cnt를 deque에 넣었는데
  list값을 바꾸면서 돌수 있다
  '''
  # 3번째 : cnt
  q = deque()
  q.append((0, 0))
  while q:
    # 현재 i, j
    ci, cj = q.popleft()
    # print(v, end = " ")
    for i, j in ((1, 0), (0, 1), (0, -1), (-1, 0)):
      di, dj = ci+i, cj+j
      if 0 <= di < n and 0 <= dj < m and ground[di][dj] == 1:
        q.append((di, dj))
        ground[di][dj] += ground[ci][cj]
  return ground[di-1][dj-1]
print(BFS())