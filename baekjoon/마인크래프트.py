# 이분탐색
import sys

N, M, B = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []
result1 = []
index = 0
for i in range(257):
    mud = int(B)
    force = 0
    for j in range(N):
        for k in range(M):
            n = i - lst[j][k]
            if n < 0:
                mud -= n
                n *= -2
            elif n > 0:
                mud -= n
            force += n
    if mud>=0:
        result.append(force) 
        result1.append(i)
        
print(min(result),  result1[len(result)-result[::-1].index(min(result))-1])