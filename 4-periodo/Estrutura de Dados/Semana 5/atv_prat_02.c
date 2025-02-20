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
    
    if(p1 > p2)
        printf("O maior endereço é o de n1: %p\n", p1);
    else
        printf("O maior endereço é o de n2: %p\n", p2);
    
    return 0;
}