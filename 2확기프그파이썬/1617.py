a = input()
b = str(a[::-1])
c = str(int(a) + int(b))
if c == c[::-1]:
    print("YES")
else:
    print("NO")