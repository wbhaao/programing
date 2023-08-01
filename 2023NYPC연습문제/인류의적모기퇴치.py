import sys
input = sys.stdin.readline

def listHandler(a, b, l):
    try:
        if a < 0 or b < 0:
            return 0
        return l[a][b]
    except:
        return 0

n, m = map(int, input().split(" "))
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
if m == 0:
    print(max(sum(arr, [])))
else:
    maximum = sum(sorted(sum(arr, []), reverse=True)[0:m*4+1])
    largest = 0
    a = 0
    printed = False
    for i in arr:
        b = 0
        for j in i:
            cross = 0
            diagonal = 0
            for i in range(1, m+1):
                cross += listHandler(a+i, b, arr)
                cross += listHandler(a-i, b, arr)
                cross += listHandler(a, b+i, arr)
                cross += listHandler(a, b-i, arr)
                diagonal += listHandler(a+i, b+i, arr)
                diagonal += listHandler(a+i, b-i, arr)
                diagonal += listHandler(a-i, b+i, arr)
                diagonal += listHandler(a-i, b-i, arr)
            cross += listHandler(a, b, arr)
            diagonal += listHandler(a, b, arr)
            b += 1
            if max(cross, diagonal) == maximum:
                print(max(cross, diagonal))
                printed = True
                break
            elif max(cross, diagonal) > largest:
                largest = max(cross, diagonal)
        a += 1
    if not printed:
        print(largest)