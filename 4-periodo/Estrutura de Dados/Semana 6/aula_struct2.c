//Struct pro ponteiros

#include<stdio.h>
#include<locale.h>

//Definição de uma estrutura
struct retangulo{
	float largura;
	float altura;
};

//Função para calcular a área do retangulo
float calcularArea(struct retangulo *r) {
	return r->largura * r->altura;
}

//Função para calcular o perímetro do retangulo
float calcularPerimetro(struct retangulo *s){
	return 2 * (s->largura + s->altura);
}

main(){
	setlocale(LC_ALL, "Portuguese");
	//Declarando uma variavel do tipo estrutura retangulo
	struct retangulo resp;
	
	//Declarando um ponteiro para struct
	struct retangulo *pret = &resp;
	
	printf("\n DIgite a largura do retangulo: ");
	scanf("%f", &pret->largura);
	printf("\n Digite a altura do retangulo: ");
	scanf("%f", &pret->altura);
	
	//Mostrando os resultados
	printf("O perimetro do retangulo é %f", calcularPerimetro(pret));
	printf("A area do retangulo é %f", calcularArea(pret));
}