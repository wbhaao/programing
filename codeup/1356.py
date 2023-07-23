n = int(input())
for i in range(n):
    for z in range(n):
        if i==0 or i==n-1 or z==0 or z==n-1:
            print('*', end="")
        else:
            print(' ', end="")
    print()