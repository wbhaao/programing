#include <stdio.h>

int main(void) {
  int start, end;
  char str[1000];
  scanf("%s", str);
  scanf("%d %d", &start, &end);
  for (int i = start-1; i < end; i++) {
    printf("%c", *(str+i));
  }
  return 0;
}