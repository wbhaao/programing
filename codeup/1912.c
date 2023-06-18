#include<stdio.h>

int f(int k, int l)
{
    if(k>l) return 1;
    return k * f(k+1, l);
}

int main()
{
    int n, m;
    
    scanf("%d", &n);
    
    printf("%d", f(1, n));
    return 0;
}
