cnt = int(input())
t = {}
 
for n in range(cnt):
    r, left, right = input().split()
    t[r] = [left, right]

# 중앙, 왼쪽, 오른쪽
def preceding(r):
    if r!='.':
        print(r, end='')
        preceding(t[r][0])
        preceding(t[r][1])
# 왼쪽, 중앙, 오른쪽
def inorder(r):
    if r!='.':
        inorder(t[r][0])
        print(r, end='')
        inorder(t[r][1])

# 왼쪽, 오른쪽, 중앙
def post(r):
    if r!='.':
        post(t[r][0])
        post(t[r][1])
        print(r, end='')
 
 
preceding('A')
print()
inorder('A')
print()
post('A')