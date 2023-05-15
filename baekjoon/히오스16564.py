n, exp = map(int, input().split())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())
lenght = len(arr)
_exp = exp
_arr = list(arr)
start = min(arr)
end = (exp//lenght+1)+(sum(arr)//lenght+1)

while start<=end:
    middle = (start+end)//2
    exp = _exp
    arr = list(_arr)
    for a in range(len(arr)):
        if arr[a] < middle:
            exp -= middle-arr[a]
            arr[a] = middle
            
            if exp<0:
                end = middle-1
                break
    if not exp<0:
        start = middle+1
print(end)