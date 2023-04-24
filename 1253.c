#include <stdio.h>
#include <math.h>
int main(){
    
    for (;;)
    {
        char n;
        scanf("%s", &n);
        if (n=='q')
        {
            printf("%c\n", n);
            break;
        }
        printf("%c\n", n);
        
    }
    return 0;
}