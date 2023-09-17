import sys
input = sys.stdin.readline

lst1 = set([])
lst2 = set([])

N, M = map(int, input().split())
for i in range(N):
    lst1.add(input())
for i in range(M):
    lst2.add(input())
answer = sorted(list(set(lst1) & set(lst2)))
print(len(answer))
for s in answer:
    print(s, end='')