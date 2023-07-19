#include<stdio.h>
int main(){
    long long int a,m,d,n;
    scanf("%lld %lld %lld %lld",&a,&m,&d,&n);
    
    for (int j = 1; j <n; j++){
        a = a*m+d;
    }
    printf("%lld",a);
    return 0;
}