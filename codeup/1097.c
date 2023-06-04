#include <stdio.h>

int a[20][20] = {};
int main() {
  int n, i, j, x, y;
  for (i = 1; i <= 19; i++) //한 줄씩 바둑판 상황 입력 받기
    for (j = 1; j <= 19; j++)
      scanf("%d", &a[i][j]);

  scanf("%d", &n); //좌표 개수 입력받기

  for (i = 1; i <= n; i++) //좌표의 개수만큼
  {
    scanf("%d %d", &x, &y);
    for (j = 1; j <= 19; j++) //가로 줄 흑<->백 바꾸기
    {
      a[x][j] = !(a[x][j]);
      a[j][y] = !(a[j][y]);
    }
  }
  for (j = 1; j <= 19; j++) //세로 줄 흑<->백 바꾸기
  {
    for (i = 1; i <= 19; i++) //세로 줄 흑<->백 바꾸기
    {
      printf("%d ", a[j][i]);
    }
    printf("\n");
  }
}

