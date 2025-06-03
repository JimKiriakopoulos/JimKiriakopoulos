//ypologismos ginomenou
#include<stdio.h>
int a,b,c;
int ginomeno(int x, int y);
main(){
	//Eisodos ginomeno 1ou arithymou
	printf("Eisagete arithmo mataski 1 kai 100:");
	scanf("%d",&a);
	
	//Eisodos ginomeno 2ou arithymou
	printf("Eisagete arithmo mataski 1 kai 100:");
	scanf("%d",&b);
	
	//to c ginomeno a kai b
	c=ginomeno(a,b);
	printf("To gimnomeno tou %d kai %d einai %d\n",a,b,c);
 }
    //H sinartisi epistefei toy ginomeno x kai y 
	int ginomeno(int x, int y){
    return (x*y);
  }

