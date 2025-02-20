#include<stdio.h>
#include<math.h>
#include<locale.h>

void relatorio(int qtd[10], float preco[10]);

int main(){
	setlocale(LC_ALL, "Portuguese");
	
	int qtdVendida[10];
	float preco[10];
	int i, posicao = 0, qtd;
	float valorObjeto;
	
	// Loop para digitar o valor e quantidade
	for(i = 0; i < 10; i++){
		printf("\n--------------------------------------------------");
		printf("\nDigite o Valor unitário da peça %i: ", i + 1);
		scanf("%f", &preco[i]);
		
		printf("Digite a quantidade vendida da peça %i: ", i + 1);
		scanf("%i", &qtdVendida[i]);
		printf("\n--------------------------------------------------");
	}
	
	printf("\n");
	relatorio(qtdVendida, preco);
	
	// Saber a posição e valor do objeto mais vendido
	for(i = 0; i < 10; i++){
		if(i == 0 || qtdVendida[i] > qtd){  
			qtd = qtdVendida[i];
			valorObjeto = preco[i];
			posicao = i + 1;  
		}
	}
	
	printf("\n");
	printf("O valor do produto mais vendido é R$ %.2f e ele se encontra na posição %i.\n", valorObjeto, posicao);

	return 0;
}

// Função para calcular os valores da venda e comissão
void relatorio(int qtd[10], float preco[10]){
	int i;
	float vlTotal, vlComissao;
	
	for(i = 0; i < 10; i++){
		vlTotal = qtd[i] * preco[i];
		printf("\n--------------------------------------------------");
		printf("\nQuantidade vendida produto %i: %i", i + 1, qtd[i]);
		printf("\nValor unitário produto %i: R$ %.2f", i + 1, preco[i]);
		printf("\nValor total da venda produto %i: R$ %.2f", i + 1, vlTotal);
		printf("\n--------------------------------------------------");
		
		vlComissao += vlTotal;
	}
	vlComissao = vlComissao * 0.05;
	printf("\nO valor da comissão será de: R$ %.2f\n", vlComissao);  
}
