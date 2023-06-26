#include <stdio.h>

struct STUDENT {
  int no;
  int inf;
  int mat;
  int sum;
  double avg;
};

int main(void) {
  int cnt;
  scanf("%d", &cnt);
  struct STUDENT lst[100];
  for (int i = 0; i < cnt; i++) {
    struct STUDENT std;
    scanf("%d %d %d", &std.no, &std.inf, &std.mat);
    std.sum = std.inf + std.mat;
    std.avg = (std.inf + std.mat) / 2.0;
    lst[i].no = std.no;
    lst[i].sum = std.sum;
    lst[i].avg = std.avg;
  }
  for (int i = 0; i < cnt; i++) {
    printf("%d %d %.1f\n", lst[i].no, lst[i].sum, lst[i].avg);
  }
  return 0;
}