N = int(input())
lst1 = []
for i in range(N):
    lst1.append(input())

K = int(input())
lst2 = []
for i in range(K):
    lst2.append(input())
reLst = []
for l in lst1:
    if l in lst2:
        reLst.append(l)
print(len(lst1)-len(reLst))
for i in lst1:
    if i in reLst:
        continue
    print(i)