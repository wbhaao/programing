def S(l):
    if len(l)==1:
        return l[0]
    return l[0] + S(l[1:])
print(S(list(map(int, input().split()))))