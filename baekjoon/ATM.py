N = int(input())
lst = sorted(list(map(int, input().split())))
sum_ = 0
answer = 0
for i in lst:
    sum_ += i
    answer += sum_
print(answer)