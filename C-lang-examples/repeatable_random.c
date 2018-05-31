#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/* repeatable random number */
int main()
{
   int i, n;
   time_t t;
   
   n = 5;
   /* randomizer initializtion */
   srand((unsigned) time(&t));

   for( i = 0 ; i < n ; i++ ) {
      printf("%d\n", rand() % 9000000+1000000);//1000000~9999999,total 9000000 numbers
      //printf("%d\n", rand() % 10);//0~9,total 10 numbers
   }
   
  return(0);
}
