#include <stdio.h>

int main(){
    int n, v;
    scanf("%d", &v);
    do{
        scanf("%d", &n);
        printf("%d\n", n);
        v-=1;
        if (v==0){
            break;
        }
    }while(1)
    return 0;
}