#include<stdio.h>
#include<stdlib.h>

#define Tam_Pilha 100

struct pilha {
	int topo;
	int itens[Tam_Pilha];
};

int empty(struct pilha *p){
	if(p->topo == -1){
		return 1;
	}
	
	return 0;
}

int pop(struct pilha *p){
	if(empty(p)){
		printf("\n Pilha Vazia");
		exit(1);
	}
	return (p->itens[p->topo]);
}

int push(struct pilha *p, int e){
	if()
}