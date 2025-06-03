#include<stdio.h>
void f1();
void f2();

int x();
// sinartish tou app
main(){
	int a=0;
	int x=5;
	printf("\n main: a=%d,x=%d",a,x);
	f1();
	printf("\n main: a=%d,x=%d",a,x);
	f2();
	printf("\n main: a=%d,x=%d",a,x);
// soma tou app
}
void f1(){
	int a=2,x=0;
	printf("\n f1: a=%d,x=%d",a,x);
}
void f2(){
	int a=8,x=7;
	printf("\n f2: a=%d,x=%d",a,x);
}
// praji ton synartiseon tou app
