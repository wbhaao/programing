T = int(input())
for i in range(T):
    N = int(input())
    if N <= 5:
        print(N//4+1)
        continue
    dp = [0]*N
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2
    for j in range(5, N):
        dp[j] = dp[j-1]+dp[j-5]
    print(dp[N-1])