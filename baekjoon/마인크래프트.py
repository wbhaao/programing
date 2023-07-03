# 이분탐색
import sys
import numpy as np

read = sys.stdin.readline
N, M, B = map(int, read().split())
lst = []
maxNum, minNum = 0, 200000000
for i in range(N):
    tmplst = list(map(int, read().split()))
    lst.append(tmplst)
    maxNum = max(max(tmplst), maxNum)
    minNum = min(min(tmplst), minNum)
print(maxNum, minNum)