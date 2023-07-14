'''
기존 BFS랑 똑같이 짬
'''

from collections import deque
import sys
read = sys.stdin.readline
M, N, H = map(int, read().split())
visited = [False] * (M * N * H)
arr = []
for i in range(H):
    arr_temp = []
    for j in range(N):
        arr_temp.append(list(map(int, read().split())))
    arr.append(arr_temp)
cnt = 0
while True:
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1 and visited[k + j*M + i*M*N] == False:
                    cnt += 1
                    for ni, nj, nk in ((1, 0, 0), (-1, 0, 0),\
                                       (0, 1, 0), (0, -1, 0),\
                                       (0, 0, 1), (0, 0, -1)):
                        mi = ni + i; mj = nj + j; mk = nk + k
                    
def BFS():
    q = deque()
    q.append(v)
    visited[v] = True
    # queue를 통해 우선순위 정하면서
    while q:
    # 현재 노드를 대기열에서 삭제
    vv = q.popleft()
    # 현재 노드 출력
    print(vv, end=" ")
    # 주변 노드 있으면 대기열에 저장 (작은순)
    for z in range(1, n+1):
        if graph[vv][z] == 1 and visited[z]==0:
            q.append(z)
            visited[z] = 1













