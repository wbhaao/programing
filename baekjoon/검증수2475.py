a = map(int, input().split())
sum = 0
for i in a:
    sum += i**2
print(sum%10)