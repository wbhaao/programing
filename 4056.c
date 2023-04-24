#include <stdio.h>

int main()
{
    int a;
    double b = 0;

    scanf("%d", &a);

    if (a > 10000)
    {
        b = 1475 + (a - 10000) * (2 / 100.0);
    }
    else if (a > 4500)
    {
        b = 1200 + (a - 4500) * (5 / 100.0);
    }
    else if (a > 1500)
    {
        b = 750 + (a - 1500) * (15 / 100.0);
    }
    else if (a > 500)
    {
        b = 350 + (a - 500) * (40 / 100.0);
    }
    else
    {
        b = a * (70 / 100.0);
    }

    printf("%d", (int)b);

    return 0;
}
