#include<stdio.h>
 
 
int main(){
    
    int a;
    int b[1000] = {};
    scanf("%d",&a);
    
    for(int i =0; i<a; i++)
    {
        scanf("%d", &b[i]);
    }
    for(int j = a-1; j >= 0; j--)
    {
        printf("%d ",b[j]);
    }
    return 0;
}
 