'''
코멘트
- 뒤부터 다음 -까지 괄호로 묶으면 되잖아
즉 한번 - 나온 이후로는 전부 마이너스로 계산한다리
천잰가 히히히히힣

이건 뭔풀이냐 진짜
개잘풀었네
'''

import sys
input = sys.stdin.readline
N = input()
minusIndex = N.find('-')
front = sum(map(int, N[:minusIndex].split("+")))
if minusIndex == -1:
    print(front)
else:
    end = sum(map(int, N[minusIndex+1:-1].replace('-', '+').split('+')))
    print(front-end)
    
    
'''
모범답안
'''
import sys
input = sys.stdin.readline
arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)