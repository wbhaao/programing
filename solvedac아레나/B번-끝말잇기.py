N = int(input())
lst1 = [0] * 101
qIndex = 0
lastIndex = 0
for i in range(N):
    lst1[i] = input()
    if lst1[i] == "?":
        qIndex = i
    lastIndex = i
M = int(input())
for z in range(M):
    a = input()
    if qIndex==0 or a[0] == lst1[qIndex-1][-1]:
        if qIndex==lastIndex or a[-1] == lst1[qIndex+1][0]:
            if a not in lst1:
                print(a)