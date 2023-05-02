
#include<stdio.h>
 
 
int main(){
    
    int a;
    int b[444] = {};
    scanf("%d",&a);
    
    for(int i =0; i<a; i++){
        scanf("%d", &b[i]);
    }
  
    for(int k = 0; k < 2; k++){
        for(int j = 0; j <a; j++){
            printf("%d\n",b[j]);
        }
    }
    
    return 0;
}