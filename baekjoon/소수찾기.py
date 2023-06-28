import sys
read = sys.stdin.readline

def is_prime_number(x):
    if x==1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True 

cnt = int(read())
lst = list(map(int, read().split()))
result = 0
for i in range(cnt):
    if is_prime_number(lst[i]):
        result += 1
print(result)