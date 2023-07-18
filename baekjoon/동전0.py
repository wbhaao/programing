import sys
input = sys.stdin.readline

N, price = map(int, input().split())
lst = []
cnt = 0
i = -1
for z in range(N):
    lst.append(int(input()))
while price>0:
    if price-lst[i] >= 0:
        cnt += 1
        price-=lst[i]
    else:
        i -= 1
print(cnt)    
    
    
    