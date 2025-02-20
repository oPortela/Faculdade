#include <stdio.h>
#include <locale.h>

main(){
	setlocale(LC_ALL, "Portuguese");
	
	int x = 42;
	int *ptr = &x;
	
	printf("Endereço de x: %p,", ptr); //Exibe endereço do ponteiro
	printf("\n COnteúdo de x: %i", *ptr); //Exibe o valor da variavel que o ponteiro aponta
}