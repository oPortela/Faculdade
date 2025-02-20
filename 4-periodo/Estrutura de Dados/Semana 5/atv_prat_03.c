/*
3. Escreva um programa que contenha duas variáveis inteiras. Leia essas variáveis do teclado. 
Em seguida, compare seus endereços e exiba o conteúdo do maior endereço ¸o.
*/

#include<stdio.h>
#include<locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    
    int n1, n2; 
    int *p1, *p2;
    
    printf("Digite o valor de n1: ");
    scanf("%d", &n1);
    
    printf("Digite o valor de n2: ");
    scanf("%d", &n2);
    
    p1 = &n1;
    p2 = &n2;
    
    //printf("%p ------- %p", p1, p2);
    
    if(p1 > p2)
        printf("O maior endereço é o de n1: %d\n", n1);
    else
        printf("O maior endereço é o de n2: %d\n", n2);
    
    return 0;
}