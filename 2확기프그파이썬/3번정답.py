def max_value(data):
    if len(data) == 0:
        return 0
    first = data[0]
    rest = max_value(data[1:])

    if first > rest:
        return first
    else:
        return rest
    
lst = list(map(int, input().split()))
print(max_value(lst))