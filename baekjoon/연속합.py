N = int(input())
lst = list(map(int, input().split()))

dp = [0] * N
dp[0] = lst[0]
for i in range(1, N):
    if lst[i] > dp[i-1]+lst[i]:
        dp[i] = lst[i]
    else:
        dp[i] = dp[i-1]+lst[i]
print(max(dp))