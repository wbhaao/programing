def Max(l):
    if len(l) == 0:
        return 0
    i = l[0]
    j = Max(l[1:])
    if i > j:
        return i
    else:
        return j
print(Max(list(map(int, input().split()))))