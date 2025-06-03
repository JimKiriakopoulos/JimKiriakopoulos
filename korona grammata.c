//korona grammata.c

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main(){
	int i;
	printf("Enter a number: ");
	scanf("%d",&i);
	
	i=i>0 ? 1: 0;
	printf("Outcome: %d",i);
	
    return 0;
}
