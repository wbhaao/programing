import random
import os
letters_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_list = ''
os.system('cls')
sample_string = input("문자열을 적어주세용 : ").replace(" ", "")
print()

while True:
    rand = random.sample(letters_set, 1)[0]
    random_list += rand
    print(rand, end="")
    if sample_string in random_list:
        break
print(random_list)