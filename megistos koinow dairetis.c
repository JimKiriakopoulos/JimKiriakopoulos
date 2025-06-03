#include <stdio.h>
int mkd(int a,int b);
main(){
	int a,b;
	printf("dose ton 1o arithmo:");
	scanf("%d",&a);
	
	printf("dose ton 1o arithmo:");
	scanf("%d",&b);
	
	printf("\no mkd einai o %d tou a=%d kai tou b=%d",mkd(a,b),a,b);
}
int mkd(int a,int b){
	
	printf("\n%d %d",a,b);
	if (a==b)
	return a;
	else if (a<b)
	return mkd(a,b-a);
	else
	return mkd(a-b,b);
}
