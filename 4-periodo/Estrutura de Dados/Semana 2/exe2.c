#include<stdio.h>
#include<math.h>
#include<locale.h>

main(){
	setlocale(LC_ALL,"Portuguese");
	
	int i, num;
	int cont = 0;
	
	for(i=0; i<10; i++){
		printf("Digite um Número: ");
		scanf("%i",&num);
		
		if(num % 2 == 0){
			cont += 1;
		}
	}
	
	printf("\n Foram digitados %i Números pares",cont);
}