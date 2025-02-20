#include<stdio.h>
#include<stdlib.h>

void display(int var, int *ptr);
void update(int *p);

int main(){
	int var = 15;
	int *ptr;
	
	ptr = &var;
	
	display(var, ptr);
	
	update(&var);
	
	display(var, ptr);
	
	printf("\n\nEnd.");
	while(1);
	return 0;
}

void display(int var, int *ptr){
	printf("\n\n");
	printf("Conteudo de var = %d\n", var);
	printf("Endereco de var = %p\n", &var);
	printf("Conteudo apontado por ponteiro = %d\n", *ptr);
	printf("Endereco apontado por ponteiro = %p\n", ptr);
	printf("Endereco de ptr = %p\n", &ptr);
}

void update(int *p){
	*p = *p + 1;
}

//Ponteiros
// *ptr : O apontado por, conteudo do endereço da variavel que ptr aponta
//  ptr : O endereço da variavel
// &ptr : O endereço do ponteiro