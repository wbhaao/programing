def F(n):
    print(n, end=" ")
    if n!=1:
        F(n-1)
F(int(input()))