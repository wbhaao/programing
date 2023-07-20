import sys
input = sys.stdin.readline

N = input()
lst = []

for i in (N[:-1]):
    lst.append(int(i))
    
lst.sort(reverse=True)
print(*lst, sep="")