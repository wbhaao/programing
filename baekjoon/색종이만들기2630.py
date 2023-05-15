from math import ceil

a = int(input())
arr2 = [[]] * a 
blue, white = 0, 0
for i in range(a):
    arr2[i] = list(map(int, input().split()))
# 처음부터 전부 1이거나 0이라면??
def slice_paper(paper, n):
    global blue
    global white
    for s in range(4):
        lst = []
        for i in range(int((n/2)+((n/2)*(s%2)))):
            for z in range(int(n/2+((n/2)*(s//2)))):
                try:
                    lst.append(paper[i][z])
                except TypeError:
                    lst.append(paper[int(z+(i*(n/2)))])
        if len(set(lst))==1:
            if lst[0]==1:
                blue += 1
            if lst[0]==0:
                white += 1
        elif n!=2:
            slice_paper(lst, n/2)
slice_paper(arr2, a)
print(f"{blue}, {white}")
# slice_paper(arr2, a)