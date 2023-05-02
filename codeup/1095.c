
#include<stdio.h>
 
int main() {
 
 
    int a[10000] = { 0, };
    int b;
 
    scanf("%d", &b);
 
    for (int i = 0; i < b; i++) {
        scanf("%d", &a[i]);
    }
    
    int temp;
 
    for (int i = 0; i < b; i++) {
        for (int j = 0; j < b - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
 
    printf("%d", a[0]);
 
 
    return 0;
}