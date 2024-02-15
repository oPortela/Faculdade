#include <iostream>

using namespace std;

int main(){
    int var1;
    int* pont1;

    var1 = 5;
    pont1 = &var1;


    cout << "Valor da variavel através do seu nome: " << var1 << endl;
    cout << pont1;

    return 0
}