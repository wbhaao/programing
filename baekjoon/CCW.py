'''
좌표 관련 문제
1->2->3
으로 이으면 어느 방향인지 알아보는 것이다

수학적으로 접근.
점 A와 점 C를 잇는 함수에 대해
B의 위치를 계산

'''
AX, AY = map(int, input().split())
BX, BY = map(int, input().split())
CX, CY = map(int, input().split())
# A, C를 지나는 함수 기울기
try:
    m = (AY - CY) / (AX - CX)
except:
    print(0)
y_intercept = -(m * AX - AY)
# 함수 식 만들었다리
# X를 넣어서 Y값 추출
y = BX*m + y_intercept
x = (-y + y_intercept)/m
if abs(y/x) > 1:
    print(1)
elif abs(y/x) < 1:
    print(-1)
else:
    print(0)