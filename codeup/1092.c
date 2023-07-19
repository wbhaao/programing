#include<stdio.h>
 
int main(){
    int i = 1;
    int a, b, c;
    scanf("%d %d %d",&a,&b,&c);
    for (i = 1; i < 9999999; i++){
        if (i%a==0 && i%b==0 && i%c==0){
            break;
        }
    }
    printf("%d",i);
    return 0;
}