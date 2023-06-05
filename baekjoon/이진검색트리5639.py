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
    if first > end:
        return
    # 루트보다 큰 값이 존재하지 않을 경우를 대비
    # 이렇게 된다면 위 if에 걸림
    # 그게 아니고 큰게 없으면 안잘라도 됨 (root 빼고)
    mid = end+1
    # 1 ~ 3까지 (임의(0, 2일때)     
    for i in range(first+1,end+1):
        # 첫번째보다 큰게 있다면
        if num_list[first] < num_list[i]:
            mid = i
            break
    
    #왼쪽 트리
    postorder(first+1, mid-1)
    #오른쪽 트리
    postorder(mid, end)
    # 중앙(은 가장 마지막)
    print(num_list[first])
# 0부터 numlist-1까지
postorder(0,len(num_list)-1)