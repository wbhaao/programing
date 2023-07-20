#include<stdio.h>

int main(){
    int a, b;
    int result = 0;
    scanf("%d",&a);
    
    for(int i = 1; i <= a; i++)
    {
        scanf("%d",&b);
        result+=b;
    }
    printf("%d",result);
    return 0;
}