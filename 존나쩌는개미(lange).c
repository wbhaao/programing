#include <stdio.h>
#include <math.h> //abs, labs, fabs
int main(void) {
    int x, y, posX, posY, t;
    scanf("%d %d %d %d %d",&x, &y, &posX, &posY, &t);

    int posXT = t/(x*2) == 0 ? t : t%(x*2);
    int posYT = t/(y*2) == 0 ? t : t%(y*2);

    posX = posX + posXT > x ? x-((posX + posXT) - x) : posX + posXT;
    posY = posY + posYT > y ? y-((posY + posYT) - y) : posY + posYT;
   
    printf("%d %d", abs(posX), abs(posY));
    
}