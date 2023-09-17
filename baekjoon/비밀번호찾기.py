from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

lst1 = dict()

for i in range(N):
    s = input().split()
    lst1[s[0]] = s[1]

for i in range(M):
    A = input()[:-1]
    print(lst1[A])