#include<stdio.h>
 
int main(){
 
    int m,n,cnt,result = 0;
    scanf("%d %d", &m, &n);

    for (int i = 1; i <= m; i++)
    {
       if (m % i == 0)
       {
            cnt++;
            
       }
       if (cnt==n)
       {
            result = i;
            break;
       }
       
       printf("%d", result);
    }
    return 0;
}