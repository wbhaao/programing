n = int(input())
for i in range((n+1)//2):
    for z in range((n+1)//2-(i+1)):
        print(" ", end="")
    for z in range((i*2)+1):
        print("*", end="")
    print(" ")