list1 = [[1, 10], [2, 22], [3, 19], [4, 7]]
list2 = [data for inner_list in list1 for data in inner_list]
print(list2)