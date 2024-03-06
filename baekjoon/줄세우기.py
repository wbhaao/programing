'''
정렬 구현 문제
'''

N = int(input())
for _ in range(N):
    arr=list(map(int,input().split()))
    total=0
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)): # i 뒤에 애들과 전부 비교해서
            if arr[i] > arr[j]:  # i가 더 크면
                arr[i],arr[j] = arr[j],arr[i]  # 자리바꾸기
                total+=1
    print(arr[0], total)