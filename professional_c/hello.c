#include <stdio.h>

void add(int *a, int b) {
    *a += b;
}

int main() {
    int a, b;scanf("%d %d", &a, &b);
    while (a < 100)
    {
        add(&a, b);        
        printf("%d\n", a);
    }
    return 0;
}