s_stack = []
b_stack = []

def checkVFC(lst, mul):
    global s_stack
    global b_stack
    # (index, 값) 형식
    for l in enumerate(lst):
        if l[1] == '(':
            s_stack.append(0)
        elif l[1] == ')':
            if len(s_stack)==0:
                print(0)
                exit()
            s_stack.pop()
        elif l[1] == '[':
            b_stack.append(0)
        elif l[1] == ']':
            if len(b_stack)==0:
                print(0)
                exit()
            b_stack.pop()
        if (lst[0]==('(' if lst[l[0]]==')' else '?') and len(s_stack)==0) or \
           (lst[0]==('[' if lst[l[0]]==']' else '?') and len(b_stack)==0):
            # 다시 연산할 수 있게 보내줌, 소괄호면 *2 대괄호면 *3
            if l[0]>1:
                return checkVFC(lst[1:l[0]], 2 if lst[0]=='(' else 3) * mul
            else:
                return checkVFC(lst[2:], mul) + 2 if lst[0]=='(' else 3

lst1 = input()
a = checkVFC(lst1, 1)
print(a)