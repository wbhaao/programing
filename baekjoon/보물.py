N = int(input())
lst1 = sorted(list(map(int, input().split())), reverse=True)
lst2 = sorted(list(map(int, input().split())))

answer = 0
for i in range(N):
    answer += lst1[i]*lst2[i]
print(answer)


