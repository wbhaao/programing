"""
stack안쓰니까 이상한 경우를 다 구해야해서 힘들었따
"""

while True:
    a = input()
    stack = []

    if a == ".":
        break

    for i in a:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
