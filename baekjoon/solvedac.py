N = int(input())
lst2 = [0] * N
lst = [0] * N
cnt = 0
for i in range(N):
    lst2[i] = int(input())
lst2.sort()
for i in range(N):
    if i >= round(N * 0.15) and i <= round(N * 0.85):
        lst[i] = lst2.pop(round(N * 0.15))
        cnt += 1
try:
    print(round(sum(lst) / cnt))
except:
    print(0)
