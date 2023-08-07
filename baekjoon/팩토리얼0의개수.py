"""

"""

N = int(input())
result = 1
answer = 0
for i in range(2, N + 1):
    result *= i
for i in reversed(str(result)):
    if i == "0":
        answer += 1
    else:
        print(answer)
        break
