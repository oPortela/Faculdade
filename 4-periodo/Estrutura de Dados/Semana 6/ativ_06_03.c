#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

struct registro{
	int matricula;
	char nome[100];
	int anoNascimento;
};


main(){
	setlocale(LC_ALL, "Portuguese");
	
	int quantidade, i;
	struct registro *alunos;
	
	printf("Informe a quantidade de alunos: ");
	scanf("%d", &quantidade);
	
	alunos = (struct registro *)malloc(quantidade * sizeof(struct registro));
	
	if(alunos == NULL){
		printf("ERRO NA ALOCAÇÃO DE MEMORIA! \n");
		return 1;
	}
	
	for(i = 0; i < quantidade; i++){
		printf("Digite o numero da matricula do %i aluno: ", i + 1);
		scanf("%d", &alunos[i].matricula);
		
		printf("Digite o nome do %i aluno: ", i + 1);
		scanf("%s", &alunos[i].nome);
		
		printf("Digite o ano de nascimento do %i aluno: ", i + 1);
		scanf("%d", &alunos[i].anoNascimento);
	}
	
	for(i = 0; i < quantidade; i++){
		printf("\n --------------------------\n");
		printf("Aluno %i: \n"
				"Matricula: %d\n"
				"Nome: %s\n"
				"Ano Nascimento: %d\n", i+1, alunos[i].matricula, alunos[i].nome, alunos[i].anoNascimento);
	}
	free(alunos);
}