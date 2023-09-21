N = int(input())

lst = list(map(int, input().split()))
sor = sorted(lst, reverse=True)

for i in lst:
    print(i, sor.index(i)+1)