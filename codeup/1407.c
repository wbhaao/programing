
#include<stdio.h>
 
 
int main(){
    char sss[101];
    scanf("%s", sss);
    for (int i = 0; sss[i] != '\0'; i++) {
        if (sss[i] != ' '){
            printf("%c", sss[i]);
        }
    }
    return 0;
}
