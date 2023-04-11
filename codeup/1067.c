
#include <stdio.h>
 
 
int main (void)
{
    int a,b,c;
 
    
    scanf("%d %d %d", &a , &b, &c);
    if( (a%2) == 0) printf("even\n"); 
    else printf("odd\n"); 
    
    if( (b%2) == 0) printf("even\n"); 
    else printf("odd\n"); 
    
    if( (c%2) == 0) printf("even"); 
    else printf("odd"); 
 
    
    return 0;
}
