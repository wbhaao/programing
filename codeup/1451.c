#include <stdio.h>
int main(){
    int a=0, b=0;
    int lst[100000001];
    scanf("%d", &a);
    for ( int i = 0; i < a; i++ ){
        scanf("%d", &lst[i]);
    }
    for ( int j = 0; j < a; j++ ){
        for ( int x = j; x < a; x++ ){
            if (lst[j] > lst[x]){
                int temp = lst[j];
                lst[j] = lst[x];
                lst[x] = temp;
            }
        }
    }
    for ( int k = 0; k < a; k++ ){
        printf("%d\n", lst[k]);
    }
    return 0;
}