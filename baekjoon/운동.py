'''
이것도 플루이드 워셜 알고리즘

'''

V, E = map(int, input().split())
#거리를 저장할 matrix
matrix = [[int(1e9)] * (V+1) for _ in range(V+1)]
for _ in range(E):
    x, y, c = map(int, input().split())
    matrix[x][y] = c

#경유지 k, 출발지 i, 도착지 j 로 3중 for문을 돌면서
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            # i->j 가 빠른지 i->k->j가 빠른지를 검사한다.
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = 1e9
for i in range(1, V+1):
   #사이클은 결국 출발지와 도착지가 같은 경우이므로 i->i를 확인
    answer = min(answer, matrix[i][i])

#최소값이 없으면 -1, 있으면 최소값을 출력
if answer == 1e9:
    print(-1)
else:
    print(answer)