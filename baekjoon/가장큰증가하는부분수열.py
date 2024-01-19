# LIS 알고리즘
'''
알고리즘
순차적으로 순회하면서
dp[i] 값을 계속 + 함
알고리즘이 잘못되었담ㄴ어ㅐ뮤ㅒ냐ㅗ해ㅑㅑㅗ랴ㅒ


'''
N = int(input())
numbers = list(map(int, input().split()))

# 왜 1이지, 0이여도 상관 X
dp = [0]*N
# 0번지까지 numbers의 최댓값은 numbers[0]
dp[0] = numbers[0]
# 1 index부터 채움
for i in range(1, N):
    # 0부터 순차적으로 검사
    for j in range(i):
        # 기준값이 더할 값보다 크다면
        if numbers[j] < numbers[i]:
            # dp[i] = 원래값(for문 n번째 전)과 dp[j]번과 numbers 더한 값 중 큰 값 고름
            dp[i] = max(dp[i], dp[j] + numbers[i])
        else:
            # numbers[i]가 더 크니 이전 값을 쓸 수 없음. numbers[i]와만 비교
            dp[i] = max(dp[i], numbers[i])
print(max(dp))
