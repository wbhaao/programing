'''
이걸 어케해야할까ㅏㅏㅏㅏㅏ
dp 써야한다
dp는 전부 점화식인가
'''
N = int(input())
lst = []
dp = [0] * 100001
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(N):
    lst.append(int(input()))
for i in range(4, max(lst)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in lst:
    print(dp[i])