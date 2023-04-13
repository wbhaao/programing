
#include <stdio.h>
 
int main ()
{
    언
    int year,mon,day, sum;
    scanf("%d %d %d ",&year , &mon, &day);
    sum = year - mon + day;    
    if( !(sum%=10) ){printf("대박");}
    else {printf("그럭저럭");}
    
 
    return 0;
}
