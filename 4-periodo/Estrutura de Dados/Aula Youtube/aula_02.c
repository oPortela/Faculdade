#include<stdio.h>
#include<stdlib.h>

/* Implementa uma lista COM cabeça onde todos os itens são alocados dinamicamente */

//Struct para um item da lista que possui um inteiro
struct ElementoLista {
	int valor;
	struct ElementoLista *prox;
};

//Define um novo tipo de dados (Item)
typedef struct ElementoLista Item;

// Prototipos das funções
void imprime(Item *cabeca);
void insereFim(Item* cabeca, int valor);
void libera(Item* cabeca);

int main(int argc, char *argv[]){
	//Cria a cabeça da lista
	Item cabeca;
	cabeca.prox = NULL;    //Vazia
	
	printf("Tamanho do item: %d\n", sizeof(Item));
	
	//Insere ao final da lista um item alocado dinamicamente
	printf("\nInserindo itens novoc na lista...\n");
	insereFim(&cabeca, 15);
	insereFim(&cabeca, 125);
	insereFim(&cabeca, 155);
	insereFim(&cabeca, 265);
	
	//Aguarda o usuario pressionar uma tecla
	system("PAUSE");
	
	//Uma função para imprimir os itens da lista
	printf("\nImprimindo itens da lista...\n");
	imprime(&cabeca);
	
	//Aguarda o usuario pressionar uma tecla
	system("PAUSE");
	
	//Uma funcao para liberar a memoria
	printf("\nLiberando memoria dos itens da lista...\n");
	libera(&cabeca);
	
	system("PAUSE");
	return 0;
}

// Funcao para insercao de item
void insereFim(Item* cabeca, int valor){
	
	//cria um ponteiro para o item e aloca dinamicamente
	Item *novo = (Item*)malloc(sizeof(Item));
	
	//Inicializa o novo item
	novo->prox = NULL;
	novo->valor = valor;
	
	printf("Item de valor %3d alocado no endereco : %000000x\n", novo->valor, novo);
	
	//Varre a lista do comeco para chegar na ultima posicao
	Item *atual = cabeca;
	while(atual->prox != NULL){
		atual = atual->prox;
	}
	
	//Chegando na ultima posicao, adiciona o novo elemnto
	atual->prox = novo;
}

//Funcao para imprimir os elementos
void imprime(Item* cabeca){
	// este item aponra para o item atual senbdo impresso
	// como o item do inicio é a cabeca, a impressao comeca no proximo item
	Item *atual = cabeca->prox;
	
	//laco que executa até o ultimo item
	int i = 0;
	while(atual != NULL){
		printf("Valor do item: %3d\n", atual->valor);
		i++;
		//Faz o atual mover para o proximo item
		atual = atual->prox;
	} 
	
	printf("Total de itens na lista: %d\n", i);
}

//Funcao para liberar a memoria
void libera(Item* cabeca){
	// ponteiro para o inicio da lista
	Item *atual = cabeca->prox;
	
	// ponteiro para o item a ser liberado
	Item *liberado;
	
	// parte do inicio da lista, eliminando todos os itens
	while(atual != NULL){
		//o liberado recebe o endereco do atual a ser liberado
		liberado = atual;
		//o atual recebe o endereco do proximo a ser liberado
		atual = atual->prox;
		printf("Liberando o item de valor %3d na posicao %000000x\n", liberado->valor, liberado);
		//libera o atual
		free(liberado);
	}
}