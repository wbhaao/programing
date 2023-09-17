N = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if lst1[i] <= lst2[i]:
        cnt += 1  
print(cnt)












