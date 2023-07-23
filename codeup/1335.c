#include<stdio.h>
 
 
int main(){
    int m;
    scanf("%d", &m);

    for (int i = 0; i < m; i++)
    {
        for (int x = 0; x < i; x++)
        {
            printf(" ");
        }
        for (int j = 0; j < m-i; j++)
        {
            printf("*");
        }
        
        printf("\n");
    }
    return 0;
}