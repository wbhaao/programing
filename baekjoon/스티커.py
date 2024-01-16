'''

'''
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    lst = [[], []]
    for i in range(2):
        lst[i] = list(map(int, input().split()))
    