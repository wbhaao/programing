#include <stdio.h>

int foo(int a, int max){
    if (a>max){
        exit(0);
    }
    printf("%d\n", a);
    foo(a+1, max);
}

int main(){
    int b = 0;
    scanf("%d", &b);
    
    foo(1, b);
    return 0;
}