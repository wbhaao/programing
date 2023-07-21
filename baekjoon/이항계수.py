N, K = map(int, input().split())
num = 1
for i in range(K):
    num *= N-i
    
def fac(K):
    if K < 2:
        return 1
    else:
        return K * fac(K-1)
    
kk = fac(K)
result = num // kk
print(result)