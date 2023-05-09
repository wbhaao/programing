#include <stdio.h>
#include <math.h>

// 시간 초과가 왜나냐

int fac(int a){
    if (a==1) return 1;
    else return fac(a-1)* a;
}

int main(){
    int a;
    scanf("%d", &a);
    if (a==0) printf("%d", 1);
    else printf("%d\n", fac(a));
}