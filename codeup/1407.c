#include<stdio.h>

int main(){
    char b[200000];
    scanf("%s", b);
    int index = 0;
    while(b[index]){
        if (b[index] != " "){
            printf("%s", b[index]);
        }
    }
    return 0;
}
