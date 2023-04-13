#include <stdio.h>

int main(){
    int a, b, c = 0;
    scanf("%d %d %d", &a, &b, &c);
    a += (int)((b+c)/60);
    b = (b+c)%60;
    printf("%d %d", a%24, b);
    return 0;
}