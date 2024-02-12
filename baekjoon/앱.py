N, M = map(int, input().split())
lst1 = [0] + list(map(int, input().split()))
lst2 = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(lst2)+1)] for _ in range(N+1)] 
result = sum(lst2) #열의 최댓값
for i in range(1, N+1):
    weight = lst1[i]
    value = lst2[i]
    for j in range(1, sum(lst2) + 1):
        if j < value:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(weight + dp[i-1][j-value], dp[i-1][j])
            
        if dp[i][j] >= M:
            result = min(result, j) 
if M != 0:
    print(result)
else:
    print(0)
