# LIS 알고리즘
'''
알고리즘
순차적으로 순회하면서
dp[i] 값을 계속 + 함
알고리즘이 잘못되었담ㄴ어ㅐ뮤ㅒ냐ㅗ해ㅑㅑㅗ랴ㅒ


'''

N = int(input())

numbers = list(map(int, input().split()))
dp = list(numbers)
dp[0] = numbers[0]
for i in range(1, N):
    prev = numbers[i]
    for j in reversed(range(i)):
        # prev 선언
        if prev > numbers[j]:
            dp[i] += numbers[j]
            prev = numbers[j]
print(max(dp))
