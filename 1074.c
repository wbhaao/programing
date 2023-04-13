#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    for(;;)
    {
        printf("%d\n", --n);
        if (n==0) break;
    }
    return 0;
}