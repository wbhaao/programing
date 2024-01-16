'''
프로그래머스에서 비슷한 문제를 풀어본 적이 있다..

'''
T = int(input())
answer = []
dp = [1,2,4] + [0]*999998
for i in range(3, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009
for _ in range(T):
    N = int(input())
    print(dp[N-1])