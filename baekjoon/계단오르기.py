N = int(input())
lst = [0]
answer = [0]*(N+1)
for i in range(N):
    lst.append(int(input()))

if len(lst) <= 3: 
    print(sum(lst))
else:
    answer[1] = lst[1]
    answer[2] = answer[1] + lst[2]
    for i in range(3, N+1):
        answer[i] = max(answer[i-3]+lst[i-1]+lst[i], answer[i-2]+lst[i])
    print(answer[-1])