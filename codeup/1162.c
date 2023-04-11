
#include <stdio.h>
 
int main ()
{
    //년,월,일, 합 정수 선언
    int year,mon,day, sum;
    scanf("%d %d %d ",&year , &mon, &day);
    sum = year - mon + day; //사주는 년 - 월+일
    
    if( !(sum%=10) ){printf("대박");} //10으로 나눈값이 0이라면 1로(참) 변환, 반대면 0으로 거짓이됨
    else {printf("그럭저럭");}// 아니면( 0 이 아니면)
    
 
    return 0;
}
