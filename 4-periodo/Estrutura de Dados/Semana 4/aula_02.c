#include <stdio.h>
#include <locale.h>

main(){
	setlocale(LC_ALL, "Portuguese");
	
	float A, B, *p1, *p2;
	
	A = 3.123;
	printf("\n Valor de A: %f", A);
	
	p1 = &A;
	printf("\n Valor de A usando p1: %f", *p1);
	
	*p1 = 2.456;
	printf("\n Novo valor de A: %f", A);
	
	p2 = p1;	
	B = *p2;
	printf("\n Valor de B: %f", B);
	
	B = 1.789;
	p2 = &B;	
	printf("\n Valor de B: %f;"
		   "\n Valor de A: %f;"
		   "\n Valor de p1: %f;"
		   "\n Valor de p2: %f.", B, A, *p1, *p2);
}