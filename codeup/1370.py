h, r = map(int, input().split())
for i in range(r):
    for z in range(h-1):
        print(" "*z, end="")
        print("*")
    for x in range(h):
        print(" "*(h-x-1), end="")
        print("*")