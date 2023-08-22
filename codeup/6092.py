import sys

input = sys.stdin.readline
answer = [0] * 23
N = input()
lst = list(map(int, input().split()))
for l in lst:
    answer[l - 1] += 1
print(*answer)
