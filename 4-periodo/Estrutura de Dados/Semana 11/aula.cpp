#include<stdio.h>
#include<stdlib.h>

typedef struct No{
	int dado;
	struct No* prox;
	struct No* ant;
}No;

//Função para criar um novo nó
No* criar_no(int valor){
	No* novo_no = (No*)malloc(sizeof(No));
	if(!novo_no){
		printf("Erro ao alocar memória!!!\n");
		exit(1);
	}
	novo_no->dado = valor;
	novo_no->prox = novo_no->ant = NULL;
	return novo_no;
}

//Função para inserir um nó no final da lista
void inserir_no_final(No** cabeca, int valor){
	No* novo_no = criar_no(valor);
	if(*cabeca == NULL){
		//lista vazia
		*cabeca = novo_no;
		novo_no->prox = novo_no->ant = novo_no;
	}
	else {
		No* ultimo = (*cabeca)->ant;
		novo_no->prox = *cabeca;
		novo_no->ant = ultimo;
		ultimo->prox = novo_no;
		(*cabeca)->ant = novo_no;
	}
}