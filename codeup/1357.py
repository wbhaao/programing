n = int(input())
for i in range(n):
    for z in range(i+1):
        print("*", end="")
    print(" ")
        
for i in range(n-1):
    for z in range(n-(i+1)):
        print("*", end="")
    print(" ")