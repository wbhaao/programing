N = int(input())
lst = [[0]+list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(1, i+2):
        try:
            lst[i][j] += max(lst[i-1][j-1], lst[i-1][j])
        except:
            lst[i][j] += lst[i-1][j-1]
print(max(lst[N-1]))


