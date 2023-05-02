#include<stdio.h>
 
int main() {
    int a[24] = {0,};
    int n;
    int m;
    scanf("%d", &n);
 
    for (int i = 1; i <= n; i++) {
        scanf("%d", &m);
        a[m] += 1;
    }
 
    for (int j = 1; j < 24; j++) {
        printf("%d ", a[j]);
    }
 
    return 0;
}