#include <stdio.h>

int a[110][110] = {};
int main() {
  int x, y, cnt, len, rc, posX, posY;
  scanf("%d %d", &x, &y);
  scanf("%d", &cnt);
  while(cnt--){ //한 줄씩 바둑판 상황 입력 받기
    scanf("%d %d %d %d", &len, &rc, &posX, &posY);

    while(len--){
      if (rc) {
        a[posX++][posY] = 1;
      } else {
        a[posX][posY++] = 1;
      }
    }
  }
  for (int j = 1; j <= x; j++) //세로 줄 흑<->백 바꾸기
  {
    for (int i = 1; i <= y; i++) //세로 줄 흑<->백 바꾸기
    {
      printf("%d ", a[j][i]);
    }
    printf("\n");
  }
}
