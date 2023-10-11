import time
from random import shuffle
word_list = ["apple is yammy", "banana is good", "city is bad", "domain is difficult", "evil is very bad"]
shuffle_cnt = 0
while True:
    shuffle(word_list)
    for i, word in enumerate(word_list):
        print("________________________")
        print(word)
        start_time = time.time()
        answer = input().strip()
        if answer=="exit":
            exit()
        end_time = time.time()
        print("________________________")
        print(round(end_time-start_time, 2), "s")
        right = 0
        for j in range(len(word)):
            try:
                if word[j]==answer[j]:
                    right += 1
            except:
                pass
        print("정확도 :",round(right/len(word)*100),"%")
        print("오타율 :",round((len(word)-right)/len(word)*100),"%")