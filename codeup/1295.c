#include <stdio.h>
int main()
{
    char n[1001];
    
    scanf("%s",n); 
    for(int i=0; n[i] != '\0'; i++)
    {
        if (n[i] >= 65 && n[i] <= 90) {
            n[i] += 32;
        }
        else if (n[i] >= 97 && n[i] <=122){
            n[i] -= 32;
        }
        printf("%c", n[i]);
    }
    return 0;
}
