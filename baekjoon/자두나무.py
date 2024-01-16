from sys import stdin

T, W = map(int, stdin.readline().split())
lst = [0]
dp = [[0]*(W+1) for _ in range(T+1)]
for _ in range(T):
    lst.append(int(stdin.readline()))

for i in range(1, T+1):
    if lst[i] == 1:
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, W+1):
        if lst[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif lst[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) 

print(max(dp[-1]))








