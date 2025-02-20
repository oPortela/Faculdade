#include<stdio.h>
#include<locale.h>

//Definição de uma estrutura
struct retangulo{
	float largura;
	float altura;
};

//Função para calcular a área do retangulo
float calcularArea(struct retangulo r) {
	return r.largura * r.altura;
}

//Função para calcular o perímetro do retangulo
float calcularPerimetro(struct retangulo r){
	return 2 * (r.largura + r.altura);
}

main(){
	setlocale(LC_ALL, "Portuguese");
	//Declarando uma variavel do tipo estrutura retangulo
	struct retangulo ret;
	
	printf("\n DIgite a largura do retangulo: ");
	scanf("%f", &ret.largura);
	printf("\n Digite a altura do retangulo: ");
	scanf("%f", &ret.altura);
	
	//Mostrando os resultados
	printf("O perimetro do retangulo é %f", calcularPerimetro(ret));
	printf("A area do retangulo é %f", calcularArea(ret));
}