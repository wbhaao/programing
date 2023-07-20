#include<stdio.h>
 
int main(){
    char a, b;
    scanf("%c %c", &a, &b);
    for(int i = a; i <= b; printf("%c ",i),i++){}
    return 0;
}
