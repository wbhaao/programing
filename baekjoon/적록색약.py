from collections import deque

N = int(input())

lst = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
areas = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            areas += 1
            letter = lst[i][j]
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            while q:
                i, j = q.popleft()
                for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0<=ii<N and 0<=jj<N and letter == lst[ii][jj] and visited[ii][jj] == 0:
                        q.append((ii, jj))
                        visited[ii][jj] = 1
print(areas, end=" ")
visited = [[0] * N for _ in range(N)]
areas = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            areas += 1
            letter = lst[i][j]
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            while q:
                i, j = q.popleft()
                for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0<=ii<N and 0<=jj<N and (letter == lst[ii][jj] or (letter=='R' and lst[ii][jj]=='G') or (lst[ii][jj]=='R' and letter=='G')) and visited[ii][jj] == 0:
                        q.append((ii, jj))
                        visited[ii][jj] = 1
print(areas)

















