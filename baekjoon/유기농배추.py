T = int(input())
M, N, K = map(int, input().split())
cnt = 0
lst = [[0]*M for i in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    lst[a][b] = 1

visited = [[0]*M for i in range(N)]
def dfs(a, b):
    if visited[a][b] == 0 and 0 <= a < N and 0 <= b < M:
        visited[a][b] = 1
        for x, y in [(a-1, b), (a, b-1), (a+1, b), (a, b+1)]:
            dfs(x, y)
        return 1
    return 0

for i in range(N):
    for j in range(M):
        cnt += dfs(i, j)