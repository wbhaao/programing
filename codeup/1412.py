string = input()
lst = [0]*26 

for s in string:
    if s >= 'a' and s <= 'z':
        lst[ord(s)-97]+=1
        
for i in range(26):
    print(f"{chr(i+97)}:{lst[i]}")