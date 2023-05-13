#include <stdio.h>

int main(){
    int a;
    scanf("%d", &a);
    for (int i = 0; i<a;i++, puts(""))
        for (int z = a-i-1; z<a; z++, printf("*"));
    return 0;
}