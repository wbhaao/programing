from collections import deque

M, N, H = map(int, input().split())
lst = []
for _ in range(H):
    lst.append([list(map(int, input().split())) for _ in range(N)])

visit_list2 = []
for _ in range(H):
    visit_list2.append([[0]*M for _ in range(N)])

q = deque()

# queue를 통해 우선순위 정하면서
for h in range(H):
    for i in range(N):
        for j in range(M):
            if lst[h][i][j] == 1:
                q.append((h, i, j, 1))
                visit_list2[h][i][j] = 1
max_depth = 0
while q:
    # 현재 노드를 대기열에서 삭제
    hh, iy, jx, depth = q.popleft()
    # 주변 노드 있으면 대기열에 저장 (작은순)
    for h, y, x in [[0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]:
        if 0<=iy+y<N and 0<=jx+x<M and 0<=hh+h<H and lst[hh+h][iy+y][jx+x] == 0:
            lst[hh+h][iy+y][jx+x] = 1
            max_depth = max(max_depth, depth)
            q.append((hh+h, iy+y, jx+x, depth+1))
            visit_list2[h][i][j] = 1
for h in range(H):
    for i in range(N):
        for j in range(M):
            if lst[h][i][j] == 0:
                print(-1)
                exit()
print(max_depth)