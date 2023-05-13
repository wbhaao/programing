#include<stdio.h>
 
int main(){
    int a;
    int b[1000] = {};
    scanf("%d",&a);
    for(int i =0; i<a; i++){
        scanf("%d", &b[i]);
    }
    for(int i =0; i<a; i++){
        for(int z =0; z<a; z++){
            printf("%d ", b[(i+z)%a]);
        }
        printf('\n');
    }
    
    return 0;
}
