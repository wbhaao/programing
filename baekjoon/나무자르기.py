n, wood = map(int, input().split())
trees = list(map(int, input().split()))

start, end  = 0, max(trees)

while start<=end:
    middle = (start+end) // 2
    get_wood = 0
    
    for tree in trees:
        if tree >= middle:
            get_wood += tree - middle

    if get_wood >= wood:
        start = middle + 1
    else:
        end = middle - 1 
print(end)

N, M = map(int, input().split())

trees = list(map(int, input().split()))

left, right = 0, max(trees)

while left <= right:
    mid = (left + right) // 2
    total = 0

    for tree in trees:
        if tree >= mid:
            total += tree - mid

    if total >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)