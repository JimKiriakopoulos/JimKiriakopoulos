//Telestes.c

main(){
	int x,y,temp,a;
	
	printf("dose tin proth metabliti: ");
	scanf("%d",&x);//���� ��� ������������ � ���� 5
	temp=x;
	printf("dose tin proth metabliti: ");
	scanf("%d",&y);//���� ��� ������������ � ���� 10
	x+=y;
	printf("%d\n",x);//���������� � ���� 15
	a=temp;
	a-=y;
	printf("%d\n",a);//���������� � ���� -5
	a= temp;
	a*=y;
	printf("%d\n",a);//���������� � ���� -50
	a= temp;
	a/=y;
	printf("%d\n",a);//���������� � ���� -5
	
	return 0;
}
