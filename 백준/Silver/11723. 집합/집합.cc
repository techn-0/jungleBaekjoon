#include <stdio.h>
#include <string.h>
int main()
{
    int M, S =0, NUM;
    char arr[21];

    scanf("%d", &M);

    for (int i = 0; i < M; i++)
    {
        scanf("%s %d", arr, &NUM);
        if (strcmp(arr, "add") == 0) S = S | (1 << (NUM - 1));
        else if (strcmp(arr, "remove") == 0) S = S & ~(1 << (NUM - 1));
        else if (strcmp(arr, "check") == 0)
        {
            if (S & (1 << (NUM - 1))) printf("1\n");
            else printf("0\n");
        }
        else if (strcmp(arr, "toggle") == 0) S = S ^ (1 << (NUM - 1));
        else if (strcmp(arr, "all") == 0) S = 1048576 - 1;
        else if (strcmp(arr, "empty") == 0) S = 0;
    }
}