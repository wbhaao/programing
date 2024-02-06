'''
좌표 관련 문제
1->2->3
으로 이으면 어느 방향인지 알아보는 것이다

수학적으로 접근.
점 A와 점 C를 잇는 함수에 대해
B의 위치를 계산

'''
def CCW(x1, y1, x2, y2, x3, y3):
    return  x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
result = CCW(x1, y1, x2, y2, x3, y3)
if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)