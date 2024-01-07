'''
좌표대로 for문 돌려가지고 1 채우기
그다음에 BFS로 각 구역 크기 구하고 출력

EZ

성곽 다른 사람 풀이 해석해야함
'''
# M 세로
M, N, K = map(int, input().split())

lst = [[0]*N for _ in range(M)]
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2): 
            lst[j][k] = 1








