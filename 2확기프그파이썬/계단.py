N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
dp = [0] * N

def w(i, N):
    if i==N:
        return
    dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i])
    w(i+1, N)

if len(lst) <= 2:
    print(sum(lst))
else:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    w(2, N)
    print(dp[-1])












