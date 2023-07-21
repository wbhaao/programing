import sys
input = sys.stdin.readline

lstA = [0]*20000001

N = int(input())
for i in map(int, input().split()):
    lstA[i] += 1
M = int(input())
lst1 = list(map(int, input().split()))
for i in lst1:
    print(lstA[i], end=" ")
