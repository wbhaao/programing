#include<stdio.h>
 
int main(){
    for(int i = 1; i <= 9;i++){
        for(int x = 2; x <= 5; x++){
            printf("%d x %d = %2d\t", x, i, x*i);
        }
        printf("\n");
    }
     
    return 0;
} 
