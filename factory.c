#include<stdio.h>
int factorial(int n);
// sinartish tou app
main(){
	int x;
	int res;
	printf("Dose enan fusiko arithmo");
	scanf("%d",&x);
	res=factorial(x);
	printf("\n%d=%d",x,res);
}// soma tou app
int factorial(int n){
	int y;
	if (n==1)
	  return 1;
	else{
	y=factorial(n-1);
	return n*y;
  }
}
// praji ton synartiseon tou app
