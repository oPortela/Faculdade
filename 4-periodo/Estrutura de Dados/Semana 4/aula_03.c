#include <stdio.h>
#include <locale.h>

main(){
	setlocale(LC_ALL, "Portuguese");
	
	int vet[] = {1,2,3,4,5};
	int *p = vet;
	int i;
	
	for(i=0; i<5; i++){
		printf("[%i]", p[i]);
		//printf("[%i]", *(p+i));
	}
}