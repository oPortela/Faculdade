#include<stdio.h>
#include<locale.h>
#include<math.h>

main(){
	int v1 = 5;
	float v2 = 24.89;
	char v3 = 'M';
	
	int *p1 = &v1;
	float *p2 = &v2;
	char *p3 = &v3;

	printf("------ Valores de cada variavel e ponteiro. ------\n");
	printf("\n Variavel inteiro: %i", v1);
	printf("\n Ponteiro inteiro: %p", p1);
	printf("\n Variavel real: %f", v2);
	printf("\n Ponteiro real: %p", p2);
	printf("\n Variavel char: %c", v3);
	printf("\n Ponteiro char: %p", p3);
	
	printf("\n\n\n\n");
	//Alteração nos valores
	
	v1 = 258;
	v2 = 1.7;
	v3 = 'L';
	
	p1 = &v1;
	p2 = &v2;
	p3 = &v3;

	printf("------ Valores de cada variavel e ponteiro modificados. ------\n");
	printf("\n Variavel inteiro: %i", v1);
	printf("\n Ponteiro inteiro: %p", p1);
	printf("\n Variavel real: %f", v2);
	printf("\n Ponteiro real: %p", p2);
	printf("\n Variavel char: %c", v3);
	printf("\n Ponteiro char: %p", p3);
}