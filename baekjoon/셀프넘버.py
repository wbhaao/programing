nums = set(range(1, 10000))
del_nums = set()  
for num in nums :
    for n in str(num):
        num += int(n)
    del_nums.add(num) 
self_nums = nums - del_nums  
for self_num in sorted(self_nums):
    print(self_num)