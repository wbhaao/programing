# 이분탐색
import sys

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
result = []
result1 = []
for i in range(minNum, maxNum+1):
    mud = int(B)
    force = 0
    for j in range(N):
        for k in range(M):
            n = i - lst[j][k]
            if n < 0:
                mud += 1
                n *= -2
            else:
                mud -= 1
            force += n
    if mud>=0:
        result.append(force) 
        result1.append(i) 
print(min(result),  result1[result.index(min(result))])