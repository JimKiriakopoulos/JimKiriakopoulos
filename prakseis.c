//prakseis.c

#include<stdio.h>

main(){
	
	int x,y,z;
	int telestis;
	
	printf("\nDwste ton 1o akeraio:");
	scanf("%d",&x);
	printf("\nDwste ton 2o akeraio:");
	scanf("%d",&y);
	printf("\nDwste tonn telesti\n 0 gia +\n 1 -\n 2 gia *\n 3 gia /\n 4 %");
	printf("\nEpilogi? ");
	scanf("%d",&telestis);
	
	if (telestis==0){
		z=x+y;
		printf("%d+%d=%d",x,y,z);
	}
	else if(telestis==1){
		z=x-y;
		printf("%d-%d=%d",x,y,z);
	}
	else if(telestis==2){
		z=x*y;
		printf("%d*%d=%d",x,y,z);
   }		
	else if(telestis==3){
		z=x/y;
		printf("%d/%d=%d",x,y,z);
	}
	else if(telestis==4){
		z=x%y;
		printf("%d%%d=%d",x,y,z);
	}
}
