N = int(input())
string = input()

point = 0
cnt = 0
while N > point:
    for i in reversed(range(1, 4)):
        if int(string[point:point+i]) > 641:
            continue
        elif string[point] == '0':
            point -= 1
            break
        else:
            point += i
            cnt += 1
            break
print(cnt)