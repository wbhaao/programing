import sys
input = sys.stdin.readline
N = int(input())
lst = []

for i in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])
    
lst.sort()

for i in range(N):
    print(lst[i][0],lst[i][1])