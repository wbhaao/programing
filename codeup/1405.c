#include<stdio.h>
 
 
int main(){
    
    int a;
    int b[1000] = {};
    scanf("%d",&a);
    for(int i =0; i<a; i++){
        scanf("%d", &b[i]);
    }
    int index = 0;
    for(int k = 0; k < a; k++){
        index = k;
        for(int j = 0; j <a; j++){
            printf("%d ",b[index]);
            index++;
            if(index == a){
                index = 0;
            }
        }
        printf("\n");
    }
    
    return 0;
}
