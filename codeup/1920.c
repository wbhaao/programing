#include <stdio.h>

int f(int k)
{
    if (k==0)  return;
    f(k/2);
    printf("%d", k%2);
    
}

int main()
{
    int n;
    
    scanf("%d", &n);
    if (n==0) {
        printf("%d", n%2);
        return 0;
    }
    f(n);
    return 0;
}
