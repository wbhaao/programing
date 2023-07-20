#include<stdio.h>
 
int main(){
    int a;
    scanf("%d", &a);
    for (double i = 0; i < a; i++)
    {
        printf("%.2lf ", i);
    }
    return 0;
}
