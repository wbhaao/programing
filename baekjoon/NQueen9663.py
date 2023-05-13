a = int(input())
arr = [[0] * a for _ in range(a)]
# a번 반복된다면 a_cnt를 올린다
a_cnt = 0


# 각 one 마다 변수를 따로 지정해야 한다
# 이건 나올때까지
# n이 a가 될때까지
def one(y, x, cnt, my_arr):
  # 퀸 놓을 수 있는곳 채우기
  my_arr[y][x] = 1
  # 아래로 향하는 대각선
  down_min = min(y, x)
  # 위로 향하는 대각선
  # -1 이유 : a는 index 최댓값보다 1 많아서
  up_min = min(a - y - 1, x)
  for i in range(1, a):
    # 초기 설정 값중 큰값이 갈 수 있는 값과 비례
    if i < a - max(y - down_min, x - down_min):
      my_arr[y - down_min + i][x - down_min + i] = 1
    if i < max(y - up_min, x - up_min):
      my_arr[y + up_min - i][x - up_min + i] = 1
    # 양대각선
    # 세로 긋기
    my_arr[i][x] = 1
    # 가로 긋기
    my_arr[y][i] = 1

  global a_cnt
  for j in range(a):
    for z in range(a):
      if my_arr[j][z] == 0:
        if cnt == a:
          a_cnt += 1
          break
        print('find 0')
        one(j, z, cnt + 1, my_arr)


one(1, 2, 1, arr)
print(a_cnt)
~