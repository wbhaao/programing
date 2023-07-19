import sys
input = sys.stdin.readline
min_ = 1
N = int(input())
for i in range(1, N+1):
    min_ *= i
print(min_//(7*24*60*60))