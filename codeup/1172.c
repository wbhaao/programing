#include <stdio.h>
 
int main (void)
{
    int a, b, c, temp;
    scanf("%d %d %d", &a, &b, &c);
    
    if(a > b){
        temp = b;
        b = a;
        a = temp;
    }
    if(b > c){
        temp = c;
        c = b;
        b = temp;
    }
    if(a > b){
        temp = b;
        b = a;
        a = temp;
    }
    printf("%d %d %d",a,b,c);
    return 0;
}