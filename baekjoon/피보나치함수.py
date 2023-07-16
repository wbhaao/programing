import sys
input = sys.stdin.readline
dp = [0] * 100
def fibo(n):	
  if n == 1 or n == 2:
    return 1
  if dp[n] != 0:
    return dp[n]
  if not n<0:
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n] 
  else:
    return 0
T = int(input())
for i in range(T):
    A = int(input())
    print(fibo(A))