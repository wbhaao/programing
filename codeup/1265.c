#include<stdio.h>

int main(){
    int a;
    scanf("%d",&a);
    for(int i = 1; i < 10; printf("%d*%d=%d\n",a,i,a*i),i++){}
    return 0;
}
