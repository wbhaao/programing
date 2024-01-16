# import sys

# input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
# for i in range(1, n + 1):
#     t[i], p[i] = map(int, input().split())

# dp = [0]*(n + 1)

# # 끝까지 순회
# for i in range(1, n + 1):
#     dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값
#     # fin_date : 일이 끝날 날짜
#     fin_date = i + t[i] - 1  # 당일 포함
#     if fin_date <= n:  # 최종일 안에 일이 끝나는 경우
#         # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
#         dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])
# print(max(dp))

'''
일이 끝날 날짜 : 당일 포함 : -1를 구하고 dp[끝날 날짜] = 더큰거(dp[끝날 날짜], dp[i-1] + p[i])
뒤에꺼 의미를 모르곘다
i일에는 일해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일 까지 얻을 수 있는 최댓값
받을 수 있는 거 vs 전에 일한거 + 일해서 얻을 수 있는거
'''


from sys import stdin
N = int(stdin.readline())
lst = [[0]]
t, p = [0] * (N+1), [0] * (N+1)
for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i - 1])
    fin_date = i + t[i] - 1
    if fin_date <= N:
        # 여기에 i 대신 fin_date를 적음
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])
print(max(dp))
