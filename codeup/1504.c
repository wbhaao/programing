#include<stdio.h>
 
int main(){
    int a;
    scanf("%d",&a);

    for(int i = 1; i <= a; i++){
        for(int j = 0; j < a; j++){
            printf("%d ", ((j%2==0?-1:1)*i)+(a*2-1)*(j%2));
        }
        printf("\n");
    }
    return 0;
}
