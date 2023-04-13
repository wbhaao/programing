/*
    C언어 Hello, World! 예제
*/
#include <stdio.h>

int main()
{
    int a,b;
    scanf("%d %d", &a, &b);
    printf("%d",a>b ? a : b);

    return 0;
}