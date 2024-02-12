N = int(input())
lst = list(map(int, input().split()))
M = int(input())
for i in range(M):
    A, B = map(int, input().split())
    if A == 1:
        for j in range(B-1, N, B):
            lst[j] = 1-lst[j]
    else:
        B -= 1  
        left, right = B-1, B+1
        while left >= 0 and right < N and lst[left] == lst[right]:
            left -= 1
            right += 1
        for j in range(left+1, right):
            lst[j] = 1-lst[j]
for i in range(N):
    print(lst[i], end = " ")
    if (i+1) % 20 == 0 :
        print()
