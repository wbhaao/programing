N = int(input())

for i in range(N):
    print(" " * (N-i-1), end="")
    print("*", end="")
    print(" " * (i*2), end="")
    print("*", end="")
    print()
for i in reversed(range(N)):
    print(" " * (N-i-1), end="")
    print("*", end="")
    print(" " * (i*2), end="")
    print("*", end="")
    if i!=0: print()