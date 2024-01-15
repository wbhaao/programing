'''
좌표대로 for문 돌려가지고 1 채우기
그다음에 BFS로 각 구역 크기 구하고 출력

EZ

성곽 다른 사람 풀이 해석해야함

가로 세로 구분 넘 어려웡
'''

from collections import deque

# M 세로
M, N, K = map(int, input().split())

lst = [[0]*N for _ in range(M)]
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2): 
            lst[j][k] = 1

size_list = []

for y in range(M):
    for x in range(N):
        if lst[y][x] == 0:
            size = 1
            q = deque()
            q.append((y, x))
            lst[y][x] = 1
            while q:
                iy, ix = q.popleft()
                for jy, jx in [(iy+1, ix), (iy-1, ix), (iy, ix+1), (iy, ix-1)]:
                    if 0 <= jy < M and 0 <= jx < N and lst[jy][jx] == 0: 
                        size += 1
                        q.append((jy, jx))
                        lst[jy][jx] = 1
            size_list.append(size)
print(len(size_list))
print(*sorted(size_list))

'''
from collections import deque

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if (0 <= ny < M) and (0 <= nx < N) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
    return cnt

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1

result = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] += 1
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))
'''



