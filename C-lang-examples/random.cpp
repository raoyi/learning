# include <iostream>
# include <ctime>
//# include <stdio.h>

# define    NUMMOD  10
//# define  NUMDEV  10000.0
using namespace std;
 int main()
 {
    srand((unsigned)time(NULL));
    for(int i=0;i<10;i++)
    {
        cout<<(rand()%NUMMOD)<<endl;
    }
    //getchar();
 }
