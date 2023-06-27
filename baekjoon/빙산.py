## 원본 코드 : 3760ms
## 바뀐 코드 : 3028ms
from collections import deque
def bfs(si, sj, v):
    q = deque()

    q.append((si,sj))
    v[si][sj]=1

    while q:
        # 배열을 매개변수로 넘기면 값을 변경할 시 argument에도 영향이 간다
        ci,cj = q.popleft()
        # 네방향, 범위내(X), 미방문, >0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if v[ni][nj]==0 and arr[ni][nj]>0:
                q.append((ni,nj))
                v[ni][nj]=1


def solve(): # 1 ~ 900000 년, 전체순회 반복작업
    for year in range(1, 900000):
        grounds = set()
        # [1] 네방향 0의 개수 카운트
        a_sub = [[0]*M for _ in range(N)]
        for i in range(1, N-1):
            for j in range(1, M-1):
                # 물은 패스
                if arr[i][j]==0:
                    continue
                # 상하좌우 탐색
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    #주변 물이 있다면
                    if arr[ni][nj]==0:
                        # 그 자리 a_sub칸 낮추기
                        a_sub[i][j] += 1 
                        grounds.add((i, j))

        # [2] 높이 낮추기
        for i, j in grounds:
          # 낮출 게 있다면
          if a_sub[i][j]>0:
              arr[i][j]=max(0, arr[i][j]-a_sub[i][j])

        # [3] 빙산 덩어리 개수 카운트
        v = [[0]*M for _ in range(N)]
        cnt=0
        for i in range(1, N-1):
            for j in range(1, M-1):
                if v[i][j]==0 and arr[i][j]>0:
                    # 주변 빙산 탐색 후 v = 1 한다
                    bfs(i, j, v)
                    cnt+=1
                    if cnt>=2: # 두 덩어리 이상...
                        return year
        if cnt==0:  # 덩어리개수 0개이면.. stop
            return 0
    # 이자리에 올 일은 없지만...
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve()
print(ans)