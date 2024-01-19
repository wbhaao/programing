from collections import deque
from copy import deepcopy
N, M, K = map(int, input().split())
lst = [list(input()) for _ in range(N)]

q = deque()
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
q.append((0, 0, 0, 1, deepcopy(visited)))
while q:
    y, x, k, depth, visit = q.popleft()
    for iy, ix in [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]:
        if 0 <= iy < N and 0 <= ix < M and visit[iy][ix] == 0:
            visit[iy][ix] = 1
            if iy==N-1 and ix==M-1:
                print(depth+1)
                exit()
            if lst[iy][ix] == '1':
                if k+1 > K:
                    continue
                else:
                    q.append((iy, ix, k+1, depth+1, deepcopy(visit)))
            else:
                q.append((iy, ix, k, depth+1, deepcopy(visit)))
            visit[iy][ix] = 0
print(-1)