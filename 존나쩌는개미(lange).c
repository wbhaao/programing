#include <stdio.h>
#include <math.h> //abs, labs, fabs
int main(void)
{
    int x, y, posX, posY, t;
    scanf("%d %d %d %d %d",&x, &y, &posX, &posY, &t);
    printf("%d %d", abs(x*((posX+t%(x*2))/x%2) - (posX+t%(x*2))%x), 
                    abs(y*((posY+t%(y*2))/y%2) - (posY+t%(y*2))%y));
    return 0;
}