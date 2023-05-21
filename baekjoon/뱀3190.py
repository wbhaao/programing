import sys
from collections import deque

queue = deque()

board_size = int(sys.stdin.readline())
apple_cnt = int(sys.stdin.readline())

apple_pos = []
for i in range(apple_cnt):
    apple_pos.append(list(map(int, sys.stdin.readline().split())))

move_cnt = int(sys.stdin.readline())

move_pos = []
move_dir = []

for i in range(move_cnt):
    a = sys.stdin.readline().split()
    move_pos.append(int(a[0]))
    move_dir.append(a[1])
direction = 90
time = 0
curX, curY = 1, 1
queue.append([curX, curY])
# 순서
# 머리 놓기
# 갈 포지션 정하기
# 방향 잡기
while True:
    # 방향 잡기
    if time in move_pos:
        if move_dir[move_pos.index(time)] == 'D':
            direction = (direction+360+90)% 360
        else:
            direction = (direction+360-90)% 360
    # 이동 알고리즘
    if direction%180==0:
        curY += int(direction/90 - 1)
    else:
        curX += int(1 - (direction-90)/90)
    # 머리 놓기
    queue.append([curX, curY])
    # 그자리에 사과가 없으면 꼬리 당기기
    if [curX, curY] != apple_pos:
        queue.popleft()
    # 벽에 부딫히는지
    if curX<=0 or curX>= board_size+1 or\
       curY<=0 or curY>= board_size+1:
        break
    # 내 몸에 부딫히는지
    _queue = deque(queue)
    _queue.pop()
    for q in _queue:
        if list(q) == [curX, curY]:
            break
    time += 1
print(time+1)