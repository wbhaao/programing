n = int(input())

cnt = 0

for i in range(n):
    lst = []
    s = input()
    now_letter = s[0]

    for l in s:
        if (l not in lst) or now_letter == l:
            lst.append(l)
            pass
        else:
            break
        now_letter = l

    if lst == list(s):
        cnt += 1
print(cnt)

        