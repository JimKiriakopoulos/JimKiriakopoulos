//nubers.c
#include<stdio.h>
main()
{
	int i,N,j;
	printf("Eisagete enan akeraio arithmo: ");
	scanf("%d",&N);
	
   for (i=1;i<=N;i++){
	  j=i*i*i;
	 printf("\n%d sto tetragono = %d",i,j);	
   }   
	printf("\n\nTelos programmatos");
}
