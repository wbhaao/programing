#include <stdio.h>

int main(){
    int a = 0;
    scanf("%d", &a);
    printf("%s", a%6==0 ? "win" : (a>=50 && a<=70 ? "win" : "lose"));
    return 0;
}