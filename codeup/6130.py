a = input()
one = a[:a.index('x')]
two = eval(a[a.index('x')+1:])
print(round(-(two/one), 2))
