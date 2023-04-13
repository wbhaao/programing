
#include<stdio.h>
 
int main(void)
{
    int A;
    scanf("%d",&A);
    
    if(A >= 90) printf("A");
    else if(A >=70) printf("B");
    else if(A >=40) printf("C");
    else printf("D");
    
    return 0;
}
