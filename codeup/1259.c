#include<stdio.h>
 
int main(){
    int a;
    scanf("%d", &a);
    int sum = 0;
    for (int i = 2; i <= a; i+=2)
    {
        sum += i;
    }
    printf("%d", sum);
    return 0;
}
