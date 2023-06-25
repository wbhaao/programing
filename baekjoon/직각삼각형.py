while True :
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break  
    max_ = max(lst)
    lst.remove(max_)  
    if lst[0] ** 2 + lst[1] ** 2 == max_ ** 2:
        print('right')
    else:
        print('wrong')