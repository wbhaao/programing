import sys

input = sys.stdin.readline
while True:
    A = input()
    state = ""
    sayd = True
    lst = [0] * 2
    if A == ".\n":
        break
    for i in A:
        if i == "(":
            state = "("
            lst[0] += 1
        elif i == ")":
            if state == "[":
                print("no")
                sayd = False
                break
            state = ")"
            lst[0] -= 1
            if lst[0] < 0:
                print("no")
                sayd = False
                break
        elif i == "[":
            state = "["
            lst[1] += 1
        elif i == "]":
            if state == "(":
                print("no")
                sayd = False
                break
            state = "]"
            lst[1] -= 1
            if lst[1] < 0:
                print("no")
                sayd = False
                break
    if sayd:
        if lst[0] == 0 and lst[1] == 0:
            print("yes")
        else:
            print("no")
