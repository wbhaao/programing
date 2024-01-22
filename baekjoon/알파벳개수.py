string = input()
lst = [0] * 26
for s in string:
    lst[ord(s)-97] += 1
print(*lst)