import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    age, name = input().split()
    lst.append((int(age), name))
# 앞에있는 값으로 정렬
lst.sort(key = lambda x: x[0])
for l in lst:
    print(l[0], l[1])