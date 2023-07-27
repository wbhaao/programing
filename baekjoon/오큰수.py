a = int(input())
lst = list(map(int, input().split()))
stack = []
result = -1
for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if  lst[i] < lst[j]:
            result = lst[j]
            print(result, end=" ")
            break
    if result == -1:
        print(result, end=" ")
print(-1, end=" ")