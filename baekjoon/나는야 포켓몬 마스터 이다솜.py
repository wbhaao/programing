import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst1 = []
for i in range(N):
    lst1.append(input())
for i in range(M):
    A = input()
    try:
        B = int(A)-1
        print(lst1[B], end='')
    except:
        print(lst1.index(A)+1, end='')

