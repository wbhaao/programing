from collections import deque

M, N, H = map(int, input().split())
lst = []
for i in range(H):
    lst.append(list(map(int, input().split())) for j in range(N))

print(lst)