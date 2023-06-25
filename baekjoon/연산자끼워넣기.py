'''
모든 경우의 수를 구해야 한다
모든 연산자를 다 구했다면 result가 더 적은지 더 많은지 측정
무조건 앞에서 부터 하니까 연산자 쓰면서 nums를 하나씩 줄이면 되겠다
+연산 쓴다면 0, 1번째 인덱스 +한 다음 2개 삭제하고 결과 앞에 insert
'''
from collections import deque
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)
numsCount = int(read())
nums = deque(list(map(int, read().split())))
operators = list(map(int, read().split()))
minNum, maxNum = 2000000000, 0
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
def DFS(nums, operators, result):
    global minNum
    global maxNum
    # 연산자 다 구했을때 // num로 매개 받은걸로 할 수 있음
    if sum(operators) == 0:
        if result>=maxNum:
            maxNum = result
        if result<=minNum:
            minNum = result
        return
    # 연산자 정하기
    for i in range(4):
        if operators[i] > 0:
            # operator 사용해서 -1
            operators[i] -= 1
            # 연산자 대입해서 나온 값 deque에 넣기
            a = nums.popleft()
            b = nums.popleft()
            nums.appendleft(eval(f"{a} {setOper(i)} {b}"))
            DFS(deque(nums), list(operators), nums[0])
DFS(deque(nums), list(operators), 0)
print(f"{minNum}\n{maxNum}")