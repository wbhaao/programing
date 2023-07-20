#include<stdio.h>
 
int main(){
    int a;
    int lst[10];
    int isFinded = 0;
    for(int i = 0; i <= 9; i++){
        scanf("%d", &a);
        lst[i] = a;
    }
    for(int i = 0; i <= 9; i++){
        if(lst[i]%5 == 0){
            isFinded = lst[i];
            break;
        }
    }
    printf("%d", isFinded);
    return 0;
}
