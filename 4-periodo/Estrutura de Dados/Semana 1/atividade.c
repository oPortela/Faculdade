#include<stdio.h>
#include<locale.h>
#include<math.h>

float calcularArea(float base, float altura) {
    return (base * altura) / 2;
}

void ordemCrescente() {    
    float a, b, c;

    printf("Digite 3 numeros:\n");
    scanf("%f %f %f", &a, &b, &c);

    if (a > c) {
        float tmp = c;
        c = a;
        a = tmp;
    }
    if (a > b) {
        float tmp = b;
        b = a;
        a = tmp;
    }
    if (b > c) {
        float tmp = c;
        c = b;
        b = tmp;
    }
    printf("Maior: %.2f, Meio: %.2f, Menor: %.2f\n", c, b, a);
}

void ordemDecrescente() {    
    float a, b, c;

    printf("Digite 3 numeros:\n");
    scanf("%f %f %f", &a, &b, &c);

    if (a < c) {
        float tmp = c;
        c = a;
        a = tmp;
    }
    if (a < b) {
        float tmp = b;
        b = a;
        a = tmp;
    }
    if (b < c) {
        float tmp = c;
        c = b;
        b = tmp;
    }
    printf("Menor: %.2f, Meio: %.2f, Maior: %.2f\n", a, b, c);
}

float equacao(){
	float a, b, c, delta, x1, x2;
	
	
	printf("Digite o valor de a: ");
	scanf("%f", &a);
	while(a == 0){
		printf("Digite novamente o valor de a: ");
		scanf("%f", &a);
	}
	
	printf("Digite o valor de b: ");
	scanf("%f", &b);
	
	printf("Digite o valor de c: ");
	scanf("%f", &c);
	
	delta = (b * b) - (4 * a * c);
	
	if(delta < 0){
		printf("A equação não possui números positivos.");
	} else if (delta == 0) {
		x1 = -b / (2*a);
	} else {
		x1 = (-b + sqrt(delta)) / (2 * a);
		x2 = (-b - sqrt(delta)) / (2 * a);
		printf("A equacao possui duas raizes: x1 = %f e x2 = %f", x1, x2);
	}
}

int main() {
    setlocale(LC_ALL, "Portuguese"); 
    
    int opcao = 99999;
    
    printf("Bem vindo ao sistema, escolha uma das opção ou clique zero para sair.\n");
    
    while(opcao != 0){
    	printf("\n----------------------------------\n");
    	printf("1 - Calcular area do triangulo.\n");
	    printf("2 - Ordenacao crescente.\n");
	    printf("3 - Ordenacao decrescente.\n");
	    printf("4 - Equacao segundo grau.\n");
	    printf("0 - Sair.\n");
		printf("----------------------------------\n");
		
	    printf("Escolha a opção: ");
	    scanf("%i", &opcao);
	    
	    switch (opcao) {
	    	float base, altura, area;
	    case 1:
		    printf("Digite o valor da base: ");
		    scanf("%f", &base);
		    printf("Digite o valor da altura: ");
		    scanf("%f", &altura);
		    
		    area = calcularArea(base, altura);
		    
		    printf("A area deste triangulo e %f\n", area);
		    break;
	    case 2:
	        ordemCrescente();	        
			break;
	    case 3:
	        ordemDecrescente();
	        break;
	    case 4:
	    	equacao();
	    	break;
	    default:
	        break;
		}
	}
}
