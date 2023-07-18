'''
알고리즘
stack을 만들고 새로 꽂을 게 거기 있는지 확인
있으면 패스
없으면 stack에 추가
한번 더 없으면 전 스택 2개 지우고 
그때 있으면 얘를 넣고 뒤에 걔 삭제
stack 길이가 k의 두배가 되면 반자르고 뒤에꺼
'''

import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
q = deque()
for index, l in enumerate(lst):
    if l in q:
        a = list(q)[-N:]
        if l not in a:
            q.append(l)
        pass
    else:
        q.append(l)
        if (len(q)>N):
            result += 1
    if len(q) >= N*2:
        for _ in range(len(q)//2):
            q.popleft()
print(result)