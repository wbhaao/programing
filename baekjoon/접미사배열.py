s = input()
lst = []
for i in range(len(s)):
    lst.append(s[i:])
lst.sort()
for i in range(len(s)):
    print(lst[i])