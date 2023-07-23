n = int(input())
for i in range(n):
    for z in range(n-i-1):
        print(" ", end="")
    print("*"*n, end="")
    print()