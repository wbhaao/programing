import sys
input = sys.stdin.readline

N, price = map(int, input().split())
lst = []
cnt = 0
for i in range(N) :               
    lst.append(int(input()))
    
for j in reversed(range(N)):
    if price - lst[j] >= 0:    
        cnt += price // lst[j]   
        price = price % lst[j]     
    if price == 0 : break    
print(cnt)    
    
    
    