#include <math.h>
#include <stdio.h>

int foo(int a, int d){
    for (int z = 1; z <= a; z++) {
      printf("%s", (int)(floor(d / powf(2, a - z))) % 2 == 0 ? "X" : "O");
    }
    printf("\n");
    if (d-1 >= 0)
    {
        foo(a, d-1);
    }
}

int main() {
  int a;
  scanf("%d", &a);
  foo(a, powf(2, a)-1)
  return 0;
}
