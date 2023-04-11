#include <stdio.h>
 
 
int main (void)
{
    
    int a,b,c, d;
    scanf("%d %d %d ",&a ,&b, &c);
    d = a + b + c;
    d %=1000; .
 
 
 
    d /= 100; 
    if( d%2 ){printf("그럭저럭");}
   
    else {printf("대박");}
    
 
    return 0;
}