a = input()
if a[0] == '"' and a[-1] == '"':
    if a.count('"') == 2:
        if len(a)==2:
            print("CE")
            exit()
        else:
            print(a[1:-1])

    else:
        print("CE")

else:
    print("CE")