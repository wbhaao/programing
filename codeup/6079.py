a = int(input())
answer = 0
for j in range(1, 1000):
    answer += j
    if a <= answer:
        print(j)
        exit()
