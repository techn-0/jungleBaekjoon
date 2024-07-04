#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, y, w, h;
    int pos[4];
    int val;

    scanf("%d %d %d %d", &x, &y, &w, &h);

    pos[0] = w - x;
    pos[1] = x;
    pos[2] = h - y;
    pos[3] = y;

    val = pos[0];

    for (int i = 1; i < 4; i++)
    {
        if (val > pos[i])
        {
            val = pos[i];
        }
    }
    printf("%d", val);

    system("pause");
}