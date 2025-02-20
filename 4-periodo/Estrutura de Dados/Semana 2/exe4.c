#include<stdio.h>
#include<math.h>
#include<locale.h>

int square(int x);

main(){
	setlocale(LC_ALL,"Portuguese");
	int i;
	for(i=0; i<=10; i++){
		printf("%i \n",square(i));	
	}
}

int square(int x){
	return x * x;
}