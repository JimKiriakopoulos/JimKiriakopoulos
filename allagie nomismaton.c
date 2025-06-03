//convert currert Currecry
#include<stdio.h>

float convert(void);
int main(void){
	printf("%f",convert());
	
	return 0;
}
float convert(void){
	float dollars;
		printf("Enter number of dollars:");
	scanf("%f",&dollars);
	return dollars/1.8;
}
 
