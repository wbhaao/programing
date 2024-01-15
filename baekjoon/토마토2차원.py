from collections import deque

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visit_list2 = [[0]*M for _ in range(N)]
q = deque()

# queue를 통해 우선순위 정하면서
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            q.append((i, j, 1))
            visit_list2[i][j] = 1
max_depth = 0
while q:
    # 현재 노드를 대기열에서 삭제
    iy, jx, depth = q.popleft()
    # 주변 노드 있으면 대기열에 저장 (작은순)
    for y, x in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if 0<=iy+y<N and 0<=jx+x<M and lst[iy+y][jx+x] == 0:
            lst[iy+y][jx+x] = 1
            max_depth = max(max_depth, depth)
            q.append((iy+y, jx+x, depth+1))
            visit_list2[i][j] = 1

for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            print(-1)
            exit()

print(max_depth)