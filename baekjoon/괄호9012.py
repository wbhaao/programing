cnt = int(input())

for i in range(cnt):
    vtc = input()
    pass1= False
    stack = []
    for v in vtc:
        if v == '(':
            stack.append(0)
        else:
            if len(stack)==0:
                print('NO')
                pass1 = True
                break
            stack.pop()
    if len(stack)==0 and pass1 == False:
        print('YES')
    elif pass1 == False:
        print('NO')