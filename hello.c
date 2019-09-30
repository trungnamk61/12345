#include <stdio.h>
int main()
{
   FILE *fptr;
   fptr = fopen("data.txt","a");
   if(fptr == NULL)
   {
      printf("Error!");               
   }
   
}
