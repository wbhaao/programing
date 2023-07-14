import sys
input = sys.stdin.readline
lst1, lst2 = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    lst1.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    lst2.append(row)
    
for row in range(N):
    for col in range(M):
        print(lst1[row][col] + lst2[row][col], end=' ')
    print()