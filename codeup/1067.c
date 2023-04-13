
#include <stdio.h>
 
 
int main (void)
{
    int a;
    scanf("%d", &a);
    printf(a<0 ? (a%2==0 ? "minus\neven" : "minus\nodd") : (a%2==0 ? "plus\neven" : "plus\nodd"));
 
    
    return 0;
}
