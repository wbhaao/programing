INF = int(1e9)

# 도시(vertex), 버스(edge) 입력받기
N = int(input())
M = int(input())

# 플로이드-워셜은 2차원 배열이 필요하다.
graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
    
for _ in range(M):
    a, b, c = map(int, input().split())
    # 더 비용이 적다면 최신화
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                
for x in range(1, N+1):
    for y in range(1, N+1):
        if graph[x][y] == INF: print(0, end=' ')
        else: print(graph[x][y], end=' ')
    print()