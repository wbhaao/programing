a = input().upper()
s = [0]*200
for w in a:
    s[ord(w)] += 1

__max = max(s)

h = chr(s.index((max(s))))

del s[s.index((max(s)))]
if __max == max(s):
    print("?")
    
else: 
    print(h)