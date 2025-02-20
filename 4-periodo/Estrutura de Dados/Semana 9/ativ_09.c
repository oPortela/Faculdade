#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Node{
	int codItem, qtdItem;
	char nomeItem[50];
	float valor;
	struct Node* next;
};


void inserir_inicio(struct Node** head_ref, int novo_codItem, int novo_qtdItem, char novo_nomeItem[50], float novo_valor){

	struct Node* novo_no = (struct Node*)malloc(sizeof(struct Node));
	novo_no->codItem = novo_codItem;
	novo_no->qtdItem = novo_qtdItem;
	novo_no->nomeItem[50] = novo_nomeItem[50];
	novo_no->valor = novo_valor;
	novo_no->next = (*head_ref);
	
	(*head_ref) = novo_no;
}


void imprimir_lista_produtos(struct Node* n){
	int i = 0;
	while(n != NULL){
		printf("Produto %d", i + 1);
		printf("Código Item: %d", n->codItem);
		printf("Nome Item: %s", n->nomeItem);
		printf("Quantidade Item: %d", n->qtdItem);
		printf("Valor Item: %f", n->valor);
		n = n->next;
		i += 1;
	}
	printf("NULL!!!\n");
}

main(){
	struct Node* head = NULL; 
	int n, i;
	int codItem, qtdItem;
	float valor;
	char nomeItem[50];
	
	printf("Quantos produtos deseja cadastrar: ");
	scanf("%d", &n);
	
	getchar();
	
	for(i=0; i<n; i++){
		printf("Digite o codigo do item %d:", i+1);
		scanf("%d", &codItem);
		
		printf("Digite o nome do item %d:", i+1);
		fgets(nomeItem, sizeof(nomeItem), stdin);
		nomeItem[strcspn(nomeItem, "\n")] = '\0';
		//scanf("%s", &nomeItem);
		
		printf("Digite a quantidade do item %d:", i+1);
		scanf("%d", &qtdItem);
		
		printf("Digite o valor do item %d:", i+1);
		scanf("%f", &valor);
		
		inserir_inicio(&head, codItem, nomeItem, qtdItem, valor);
	}

	printf("----- Lista encadeada -----\n");
	imprimir_lista_produtos(head);
}
