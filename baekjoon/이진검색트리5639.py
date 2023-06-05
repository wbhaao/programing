import sys
# 재귀 더 많이 쓸 수 있게 해줌
sys.setrecursionlimit(10**6)
num_list = []
# 입력받기
while True:
    try:
        num_list.append(int(input()))
    except:
        break

def postorder(first,end):
    # 
    if first>end:
        return
    mid = end+1
    f, e = int(first), int(end)
    while f<=e:
        middle = (f+e)//2
        if num_list[first] < num_list[middle]:
            e = middle-1
            mid = middle
        else:
            f = middle+1
           
    # 전위
    postorder(first+1, mid-1)
    # 후위
    postorder(mid, end)
    print(num_list[first])
# 0부터 numlist-1까지
postorder(0,len(num_list)-1)