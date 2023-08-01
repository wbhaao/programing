#include "stdio.h"
 
 
int main()
{
    int arr[101][101];
    int num;
    scanf("%d", &num);
    int x = 1;
    for(int i = 1; i <=num; i++){
        for(int j = 1; j<= num; j++){
            arr[j][i] = x;
            x++;
        }
    }
    for(int i = 1; i <=num; i++){
        for(int j = 1; j<= num; j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
