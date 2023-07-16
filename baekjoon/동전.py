import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    # 동전 개수
    N = int(input())
    coins = list(map(int, input().split()))
    # 맞춰야 핧 금액
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])