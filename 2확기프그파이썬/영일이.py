import sys
input = sys.stdin.readline

lst = [[0] * 19 for _ in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    lst[x-1][y-1] = 1
for i in range(19):
    print(*lst[i])
