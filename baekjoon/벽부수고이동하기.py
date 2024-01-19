'''
근데 3차원말고 q에 w 집어넣으면 안되나??????
해보자!
라고 하기엔 너무 피곤하다........
음..
주석달아야지
'''

from collections import deque

N, M = map(int, input().split())
K = 1
lst = [list(input()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [[[0]*(K+1) for _ in range(M)] for __ in range(N)]
queue = deque([(0, 0, 0)])

# 초기 설정
visited[0][0][0] = 1

while queue:
    x, y, w = queue.popleft()

    # 끝에 도달한 경우
    if x == N-1 and y == M-1:
        print(visited[x][y][w])
        exit(0)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if lst[nx][ny] == '1' and w < K and visited[nx][ny][w+1] == 0:
            visited[nx][ny][w+1] = visited[x][y][w] + 1
            queue.append((nx, ny, w+1))
        elif lst[nx][ny] == '0' and visited[nx][ny][w] == 0:
            visited[nx][ny][w] = visited[x][y][w] + 1
            queue.append((nx, ny, w))

print(-1)
