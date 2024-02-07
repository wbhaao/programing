from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(M):
    i, j = map(int, input().split())
    if i==j:
        print(lst[j-1])
        continue
    print(sum(lst[i-1:j]))