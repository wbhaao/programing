a = input()
a = a[1]+a[0]
a = str(int(a)*2)
if len(a) == 3:
    a = a[1:]
print(int(a))
if int(a) > 50:
    print("OH MY GOD")
else:
    print("GOOD")