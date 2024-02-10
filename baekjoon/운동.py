INF = int(1e9)

N = int(input())
M = int(input())

# [i][j] 일 때 i에서 j로 가는 비용을 나타낸다.
graph = [[INF if i != j else 0 for j in range(N)] for i in range(N)]
for _ in range(N):
    line = list(map(int, input().split()))
    for i, connected in enumerate(line):
        if connected:
            graph[_][i] = 1

# 플로이드-워셜 알고리즘
for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 여행 계획
plan = list(map(int, input().split()))

# 여행 계획이 가능한지 확인
# 차이점 .. plan[i]-1에서 -1을 붙이지 않음, indexError 가 뜬다
for i in range(M-1):
    if graph[plan[i]-1][plan[i+1]-1] == INF:
        print("NO")
        exit(0)

print("YES")
