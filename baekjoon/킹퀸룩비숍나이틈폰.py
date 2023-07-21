lst = [1, 1, 2, 2, 2, 8] 
a = list(map(int, input().split()))
for li, ai in zip(lst, a):
    print(li - ai, end=' ')