#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    n += 1;

    while(1)
    {
        printf("%d\n", (char)(--n));
        if (n==1) break;
    }
    return 0;
}