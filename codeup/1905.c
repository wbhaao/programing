#include<stdio.h>

void f(int k, int l)
{
    if(k>l) return;
    if(k%2==1) printf("%d ", k);
    f(k+1, l);
}

int main()
{
    int n, m;
    
    scanf("%d %d", &n, &m);
    
    f(n, m);
    return 0;
}
