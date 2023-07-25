import sys
input = sys.stdin.readline
N = int(input())
lst = []

for i in range(N):
    a, b = map(int, input().split())
    lst.append([b, a])
    
lst.sort(key= lambda x : (x, x[0])) 

for i in range(N):
    print(lst[i][1],lst[i][0])