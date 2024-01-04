'''
N 미만의 지역은 없는 지역으로 침
BFS를 써서 지역 개수 세기
이중 for문으로 전부 돌기
visited로 간 지역 체크
'''
'''
이거 한번 더 봐야함
'''
from collections import deque

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

max_cnt = -1
for k in range(0, max(sum(lst, []))+1):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] >= k and visited[i][j] == 0:
                cnt += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    y, x = q.popleft()
                    for iy, ix in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                        if 0 <= iy < N and 0 <= ix < N and lst[iy][ix] >= k and visited[iy][ix] == 0:
                            q.append((iy, ix))
                            visited[iy][ix] = 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)