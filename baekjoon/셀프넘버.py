numbers = set(range(1, 10000))
remove_set = set()  
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num) 
self_numbers = numbers - remove_set  
for self_num in sorted(self_numbers):
    print(self_num)