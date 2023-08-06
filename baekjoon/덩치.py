N = int(input())
lst = []
gList = [1] * N
for i in range(N):
    lst.append(list(map(int, input().split())))
for i in range(N):
    grade = 1
    for j in range(i, N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            gList[i] += 1
        if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
            gList[j] += 1
print(*gList)
