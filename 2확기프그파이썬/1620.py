n = list(map(int, list(input())))
a = 1000
while len(str(a))!=1:
    a = sum(n)
    n = list(map(int, list(str(a))))
print(a)