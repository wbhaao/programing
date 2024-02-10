N = int(input())
house_rgb = [list(map(int, input().split())) for _ in range(N)]
ans = I = 1e9
for i in range(3):
    dp = [[I, I, I] for _ in range(N)]
    dp[0][i] = house_rgb[0][i]
    for j in range(1, N):
        dp[j][0] = house_rgb[j][0] + min(dp[j-1][1],dp[j-1][2])
        dp[j][1] = house_rgb[j][1] + min(dp[j-1][0],dp[j-1][2])
        dp[j][2] = house_rgb[j][2] + min(dp[j-1][0],dp[j-1][1])
    for k in range(3):
        # r, g, b인 경우에서 최솟값 찾기
        if i != k:
            ans = min(ans, dp[-1][k])
print(ans)
