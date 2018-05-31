#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAXN 9

/* nonredundant random number */
int main()
{
   int num[MAXN+1] = {0};
   int i, n, a;
   time_t t;
   
   n = 5;
   
   /* randomizer initializtion */
   srand((unsigned) time(&t));

   for( i = 0 ; i < n ;) {
      //a = rand() % 9000000+1000000;//1000000~9999999,total 9000000 numbers
      a = rand() % 10;//0~9,total 10 numbers
      if(num[a]== 0) {
        num[a] = 1;
        i++;
      }
   }
   for( i = 0 ; i < MAXN+1 ; i++ ) {
      if(num[i]==1)
        printf("%d\n", i);
   }
  return(0);
}
