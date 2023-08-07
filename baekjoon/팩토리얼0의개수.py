"""
2*5를 찾아서 푸는 방법도 있다.
근데 이방법도 있는데
딴 방법도 신기하다
사실 그래 풀라고 실버5인데 이러면
한 브1정도
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
