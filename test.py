lst = "asdasdas"

print(lst.rindex('a'))
print(len(lst)-lst[::-1].index('a')-1)
