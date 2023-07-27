import sys
from collections import Counter

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
count = Counter(A) 
stack = []
# 비교당할 애
stack.append(0)
# 1부터 n-1까지ㄴ
# A[i]는 1, 2, 3
# count[A[i]]는 그 숫자가 등장한 번수
for i in range(1, n):
    while stack and count[A[i]] > count[A[stack[-1]]]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)