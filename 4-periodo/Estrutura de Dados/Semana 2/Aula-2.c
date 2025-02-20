/*
 Hello
*/

#include<stdio.h>
#include<math.h>
#include<locale.h>

main(){
//Setar a linguagem 
    setLocale(LC_ALL, "Portuguese");
//Declaração de variaveis
    int numero;
    float nota;
    char nome[10];
//Entrada de dados
    printf("\n Digite o nome do aluno: ");
    scanf("%s",&nome);
    fflush(stdin);
    printf("\n Digite a nota do Aluno %s.", nome);
    scanf("%f",&nota);
    printf("\n Digite um número: ");
    scanf("%i",&numero);
//Processamento de Dados
//Saida de dados
    printf("\n\t Aluno: %s",nome);
    printf("\n\t Nota: %.2f",nota);
    printf("\n\t Número: %i",numero); 
};
