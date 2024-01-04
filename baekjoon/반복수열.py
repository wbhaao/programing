'''
tag : 수학, 구현

lst에서 겹치는 부분 제외 남은 수
브루트 포스 느낌

수를 추가할때마다 겹치는 부분이 있는지 체크
겹친다면 index 출력 (index가 length)
'''

A, P = map(int, input().split())

def digit_multi(num):
    mul = 0
    for n in str(num):
        mul += int(n)**P
    return mul

lst = [A]
while True:
    dig = digit_multi(lst[-1])
    try:
        idx = lst.index(dig)
        print(idx)
        exit(0)
    except ValueError:
        lst.append(dig)
    