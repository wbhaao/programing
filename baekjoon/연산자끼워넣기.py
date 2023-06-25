'''
모든 경우의 수를 구해야 한다
모든 연산자를 다 구했다면 result가 더 적은지 더 많은지 측정
무조건 앞에서 부터 하니까 연산자 쓰면서 nums를 하나씩 줄이면 되겠다
+연산 쓴다면 0, 1번째 인덱스 +한 다음 2개 삭제하고 결과 앞에 insert

오류 : 함수 돌리기 전에 list를 번형하면 전에 애가 영향을 받아서 
연산자가 하나 없는 상태로 함수돌림

해결법  1. 함수 시작에 list를 변형
            - outOper라는 매개변수를 만들어서 활용
:       2. 

왜 48이 나올까

'''
import math
from collections import deque
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)
numsCount = int(read())
nums = deque(list(map(int, read().split())))
operators = list(map(int, read().split()))
minNum, maxNum = 2000000000, -2000000000
def setOper(i):
    if i==0:
        return '+'
    elif i==1:
        return '-'
    elif i==2:
        return '*'
    else:
        return '/'
# num을 deque로 쓸 수 있음
def DFS(depth, total, plus, minus, multiply, divide):
    global minNum, maxNum
    # 연산자 다 구했을때 // num로 매개 받은걸로 할 수 있음
    if depth == numsCount:
        maxNum = max(total, maxNum)
        minNum = min(total, minNum)
        return
    # 연산자 정하기
    if plus:
        DFS(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        DFS(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        DFS(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        DFS(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)

DFS(1, nums[0], operators[0], operators[1], operators[2], operators[3])
print(f"{(int(maxNum))}\n{int(minNum)}")