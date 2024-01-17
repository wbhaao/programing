n = int(input())

for i in range(1, n+1): # 1 ~ 9
    for z in range(1, n+1):
        if z >= i:
            print("*", end="")
    print("")
        