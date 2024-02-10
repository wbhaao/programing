INF = int(1e9)

# 도시(vertex), 버스(edge) 입력받기
N = int(input())
M = int(input())

# [i][j] 일 때 i에서 j로 가는 비용을 나타낸다.
graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
    
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            #[3][1] vs [3][2] -> [2][1]
            #중간 과정을 추가하는게 더 빠른지 검사
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                
for x in range(1, N+1):
    for y in range(1, N+1):
        # 할당되지 않았다면 0 출력
        if graph[x][y] == INF: print(0, end=' ')
        else: print(graph[x][y], end=' ')
    print()