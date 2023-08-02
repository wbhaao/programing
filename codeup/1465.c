#include "stdio.h"
 
int main(void)
{
    int arr[101][101];
    
    int n, m;
    scanf("%d %d", &n , &m);
    int x = 1;
    for(int i = 1; i <=n; i++){
        for(int j = 1; j <=m; j++){
            arr[i][j] = x;
            x++;
        }
    }
    
    for(int i = n; i >= 1; i--){
        for(int j = 1; j <= m ; j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}