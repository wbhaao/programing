dp = [0] * 10000000
dp[1] = 0
N = int(input())
for i in range(1, 1000000):
    if dp[i+1] == 0 or dp[i]+1 < dp[i+1]:
        dp[i+1] = dp[i]+1
    if dp[i*2] == 0 or dp[i]+1 < dp[i*2]:
        dp[i*2] = dp[i]+1
    if dp[i*3] == 0 or dp[i]+1 < dp[i*3]:
        dp[i*3] = dp[i]+1
print(dp[N])