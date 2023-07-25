a = input()
a_temp = str(a)
for s in a:
    print(chr(ord(s)+2), end="")
print()
a = a_temp
for s in a:
    print(chr((ord(s) * 7) % 80 + 48), end="")