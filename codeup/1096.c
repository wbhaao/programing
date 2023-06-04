#include <stdio.h>

int a[20][20]={};
int main(){
  int n, i, j, x, y;
  
  scanf("%d", &n);
  for(i=1; i<=n; i++)
  {
    scanf("%d %d", &x, &y);
    a[x][y]=1;
  }
  for(i=1; i<=19; i++) 
  {
    for(j=1; j<=19; j++) 
    {
      printf("%d ", a[i][j]);
    }
    printf("\n"); 
  }
}

