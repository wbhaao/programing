'''
아니 이게 정답이라고?? 그리디 알고리즘은 대체 뭐냐
그냥 브루트 포스 짫은 버전 아닝가

KEY CODE
lst.sort(key= lambda x : (x, x[1])) 
'''
import sys
input = sys.stdin.readline

N = int(input())
lst = []
result = 0
curTime = -1
for i in range(N):
    lst.append(list(map(int, input().split()))[::-1])
lst.sort(key= lambda x : (x, x[1])) 
for i in lst:
    if i[1] >= curTime:
        curTime = i[0]
        result += 1
print(result)