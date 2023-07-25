a = int(input())
result = 1
if a==1 or a==0:
    print(1)
    exit()
for i in range(2, a+1):
    result *= i
print(result)