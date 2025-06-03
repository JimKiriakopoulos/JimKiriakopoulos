//Telestes.c

main(){
	int x,y,temp,a;
	
	printf("dose tin proth metabliti: ");
	scanf("%d",&x);//έστω ότι καταχωρείται η τιμή 5
	temp=x;
	printf("dose tin proth metabliti: ");
	scanf("%d",&y);//έστω ότι καταχωρείται η τιμή 10
	x+=y;
	printf("%d\n",x);//εφανίζεται η τιμή 15
	a=temp;
	a-=y;
	printf("%d\n",a);//εφανίζεται η τιμή -5
	a= temp;
	a*=y;
	printf("%d\n",a);//εφανίζεται η τιμή -50
	a= temp;
	a/=y;
	printf("%d\n",a);//εφανίζεται η τιμή -5
	
	return 0;
}
