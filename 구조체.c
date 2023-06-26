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
    scanf("%d %d %d", &(lst[i].no), &lst[i].inf, &lst[i].mat);
    lst[i].sum = lst[i].inf + lst[i].mat;
    lst[i].avg = (lst[i].inf + lst[i].mat) / 2.0;
  }
  for (int i = 0; i < cnt; i++) {
    printf("%d %d %.1f\n", lst[i].no, lst[i].sum, lst[i].avg);
  }
  return 0;
}