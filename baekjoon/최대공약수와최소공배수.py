import sys
read = sys.stdin.readline

a, b = map(int, read().split())

result1 = min(a, b)
result2 = max(a, b)
for i in range(result1, 0, -1):
    if a%i == 0 and b%i == 0:
        print(i)
        break
for i in range(1, 9999999):
    if result1*i%result2 == 0:
        print(result1*i)
        break