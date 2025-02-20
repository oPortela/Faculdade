#include<stdio.h>
#include<stdlib.h>

//Criando uma estrutura da lista encadeada

struct Node{
	int data;
	struct Node* next;
};

//Função para adicionar um novo nó no início da lista
void inserir_inicio(struct Node** head_ref, int new_data){
	//Alocando memória para o novo nó
	struct Node* novo_no = (struct Node*)malloc(sizeof(struct Node));
	
	//Inserindo o dado dentro do nó criado
	novo_no->data = new_data;
	
	//Faz o próximo do novo nó ser o antigo nó
	novo_no->next = (*head_ref);
	
	//Muda o head para ser o novo
	(*head_ref) = novo_no;
}

//Função para imprimir a lista criada
void imprimir_lista(struct Node* n){
	while(n != NULL){
		printf("%d -> ", n->data);
		n = n->next;
	}
	printf("NULL!!!\n");
}

//Criando o programa principal 
/*main(){
	struct Node* head = NULL; //Inicialmente a lista está vazia, por isso recebe NULL
	
	//Inserindo elementos na lista
	inserir_inicio(&head, 10);
	inserir_inicio(&head, 20);
	inserir_inicio(&head, 30);
	inserir_inicio(&head, 40);
	inserir_inicio(&head, 5);
	inserir_inicio(&head, 3);
	inserir_inicio(&head, 1);
	
	//Imprimindo a lista
	printf("----- Lista encadeada -----\n");
	imprimir_lista(head);
}*/

main(){
	struct Node* head = NULL; //Inicialmente a lista está vazia, por isso recebe NULL
	int n, valor, i;
	
	printf("Quantos elementos deseja inserir na lista: ");
	scanf("%d", &n);
	
	//Inserindo elementos na lista
	for(i=0; i<n; i++){
		printf("Entre com o valor do elemento %d:", i+1);
		scanf("%d", &valor);
		inserir_inicio(&head, valor);
	}
	
	//Imprimindo a lista
	printf("----- Lista encadeada -----\n");
	imprimir_lista(head);
}


/*
struct aluno{
	int mat;
	char nome[50];
	float n1, n2, n3, media;
	struct aluno* prox;
};*/