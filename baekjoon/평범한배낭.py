'''

'''

'''
바텀업 방식의 코드
'''
N, K = map(int, input().split())

thing = [[]]
result = [[0]*(K+1) for _ in range(N+1)]

for _ in range(N):
    thing.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = thing[i][0]
        value = thing[i][1]

        if j < weight:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j], result[i-1][j-weight]+value)

print(result[N][K])




