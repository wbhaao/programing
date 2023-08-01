#include<stdio.h>
 
int main(){
    int N;
    scanf("%d", &N);
    int answer = 0;
    int temp = 0;
    for(int i = 1; i <= N;i++)
    {
        temp += i;
        answer += temp;
    }
    printf("%d", answer);
    return 0;
}