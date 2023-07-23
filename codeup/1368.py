H, K, rl = input().split()
H = int(H)
K = int(K)
if rl=='L':
    for i in range(H):
        for z in range(i):
            print(" ", end="")
        print("*"*K, end="")
        print()
else:
    for i in range(H):
        for z in range(H-i-1):
            print(" ", end="")
        print("*"*K, end="")
        print()