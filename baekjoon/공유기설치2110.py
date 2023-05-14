n, routers = map(int, input().split())
pos = [0]*n

for i in range(n):
    pos[i] = int(input())

pos.sort()

start = 1
end = max(pos) - min(pos)

def find_value(current_index, installCnt, middle):
    if max(pos) < middle*(routers-installCnt) + pos[current_index]:
        return -1
    if installCnt == routers:
        return 1
    for i in range(len(pos)-current_index):
        try:
            next_index = pos.index(pos[current_index] + middle + i)
        except: continue 
        return find_value(next_index, installCnt+1, middle)
    return -1
while start<=end:
    middle = (start+end)//2

    fV = find_value(0, 1 ,middle)

    if fV == 1:
        start = middle+1
    else:
        end = middle-1
print(end)