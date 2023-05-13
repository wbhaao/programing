#include <stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    int c = (a * 60) + b + 1410;
    printf("%d %d", c/60%24, c%60);
    return 0;
}