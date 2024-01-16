'''
프로그래머스에서 비슷한 문제를 풀어본 적이 있다..

'''
T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    if N<3:
        answer.append(N + N//3)
        continue
    lst = [1,2,4]
    key = 0
    
    for i in range(4, N+1):
        lst[key] = lst[0] + lst[1] + lst[2]
        key = (key+1)%3
    answer.append(lst[(key-1)%3])
for i in answer:
    print(i)