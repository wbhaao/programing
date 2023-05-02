#include <math.h>
#include <stdio.h>

int main() {
  int a;
  scanf("%d", &a);
  int c = powf(2, a);
  for (int i = c - 1; i >= 0; i--) {
    for (int z = 1; z <= a; z++) {
      printf("%s", (int)(floor(i / powf(2, a - z))) % 2 == 0 ? "X" : "O");
    }
    printf("\n");
  }
  return 0;
}
