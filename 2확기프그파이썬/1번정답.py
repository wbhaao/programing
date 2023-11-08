lst = list(map(int, input().split()))

def Sum1(data):                     
    if len(data) <= 1:
        return data[0]
    else:
        return data[0] + Sum1(data[1:])
print(Sum1(lst))
