result = []

def check(result, addStr):
    temp = "".join(result) + addStr
    for i in range(1, len(temp) // 2 + 1):
        if temp[-2 * i : -1 * i] == temp[-1 * i :]:
            return False
    return True

def dfsSearch():
    global result
    if len(result) == n:
        print("".join(result))
        exit()

    for i in range(1, 4):
        if check(result, str(i)):
            result.append(str(i))
            dfsSearch()
            result.pop()

n = int(input())
dfsSearch()