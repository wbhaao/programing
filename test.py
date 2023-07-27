a = "ab>d"
i = 1
i += a[i:].index(">")+1
print(a[i])