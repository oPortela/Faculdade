#include<stdio.h>
#include<math.h>
#include<locale.h>

/*main(){
	setlocale(LC_ALL,"Portuguese");
	
	int vetor[3];
	int i;
	
	for(i=1; i<=3; i++){
		printf("Digite o %i número: ",i);
		scanf("%i",&vetor[i]);
	}
	
	for(i=0; i<3; i++){
		printf("	%i	[%i]", i,vetor[i]);
	}
}*/

int main() {
    setlocale(LC_ALL, "Portuguese");

    int vetor[3];
    int i, posicao;

    // Corrigido o loop para começar do índice 0
    for (i = 0; i < 3; i++) {
        printf("Digite o %i numero: ", i + 1);
        scanf("%i", &vetor[i]);
    }

    // O segundo loop também está correto
    for (i = 0; i < 3; i++) {
        printf("%i,", vetor[i]);
    }

	for(i=0; i<15; i++){
		if()
	}
    //return 0;
}
