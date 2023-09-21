N = int(input())
lst = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        print(lst[(j+i)%N], end=" ")
    print()