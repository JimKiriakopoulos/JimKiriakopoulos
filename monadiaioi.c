// monadiaioi.c

#include <stdio.h>

main(){
	int x=0;
	int y=x;
	
	printf("%d,%d",x++,++y);
	printf("\n%d,%d",x++,++y);
	printf("\n%d,%d",x--,y--);
	printf("\n%d,%d",x--,--y);
}
