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
	strcpy(novo_no->nomeItem, novo_nomeItem);  
	novo_no->valor = novo_valor;
	novo_no->next = (*head_ref);
	
	(*head_ref) = novo_no;
}


void imprimir_lista_produtos(struct Node* n){
	int i = 0;
	while(n != NULL){
		printf("Produto %d:\n", i + 1);
		printf("Código Item: %d\n", n->codItem);
		printf("Nome Item: %s\n", n->nomeItem);
		printf("Quantidade Item: %d\n", n->qtdItem);
		printf("Valor Item: %.2f\n", n->valor);
		n = n->next;
		i += 1;
	}
	printf("NULL!!!\n");
}

int main(){
	struct Node* head = NULL; 
	int n, i;
	int codItem, qtdItem;
	float valor;
	char nomeItem[50];
	
	printf("Quantos produtos deseja cadastrar: ");
	scanf("%d", &n);
	
	getchar();  // Limpa o buffer do teclado
	
	for(i = 0; i < n; i++){
		printf("Digite o código do item %d: ", i + 1);
		scanf("%d", &codItem);
		
		getchar();  // Limpa o buffer após ler o código
		
		printf("Digite o nome do item %d: ", i + 1);
		fgets(nomeItem, sizeof(nomeItem), stdin);
		nomeItem[strcspn(nomeItem, "\n")] = '\0'; 
		
		printf("Digite a quantidade do item %d: ", i + 1);
		scanf("%d", &qtdItem);
		
		printf("Digite o valor do item %d: ", i + 1);
		scanf("%f", &valor);
		
		inserir_inicio(&head, codItem, qtdItem, nomeItem, valor);  
	}

	printf("----- Lista encadeada -----\n");
	imprimir_lista_produtos(head);
	
}
