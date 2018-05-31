#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    int i,j, a, min, max, size, listl;

    printf("enter a min num:");
    scanf("%d", &min);
    printf("enter a max num:");
    scanf("%d", &max);
    printf("how many num do you want:");
    scanf("%d", &listl);

    int list[listl];

    size = max - min + 1;

    srand(time(NULL));
    for(i = 0; i < listl; i ++)
    {
        while(1)
        {
            a = rand()%size+min;
            for(j = 0; j < i; j ++)
                if(list[j] == a) break;
                 
            if(j == i)
            {
                list[i] = a;
                break;
            }
        }
    }
    for(i = 0; i < listl; i ++)
        printf("%d\n",list[i]);
     
    return 0;
}
