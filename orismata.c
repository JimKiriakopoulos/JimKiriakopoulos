#include<stdio.h>
int square(int x);
// sinartish tou app
main(){
	int a=5;
	int b=10;
	int teta,tetb,sum;
	teta=square(a);
	tetb=square(b);
	sum=teta+tetb;
	printf("\n %d^2+%d^2 = %d",a,b,sum);
}// soma tou app
int square(int x){
	int y;
	y=x*x;
	return y;
}
// praji ton synartiseon tou app

