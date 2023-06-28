import sys
read = sys.stdin.readline
a = int(read())
lst = []
min_ = 8000001
for _ in range(a):
  lst.append(list(map(int, read().split())))
for i in range(a-1):
  for j in range(i+1, a):
    result = (lst[i][0] - lst[j][0])**2 +\
    (lst[i][1] - lst[j][1])**2 
    if result < min_:
      min_ = result
print(min_)
