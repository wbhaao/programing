
#include <stdio.h>
 
 
int main ()
{
    int a[7] = {0,};
    int sum = 0;
    int min = 9999999;
    for (int i = 0; i<7; i++){
        scanf("%d", &(a[i]));
        if (a[i]%2==1){
            sum += a[i];
            if (a[i]<min){
            min = a[i];
        }
        }
        
    }
    
    printf("%d\n%d", sum, min);
    return 0;
}
