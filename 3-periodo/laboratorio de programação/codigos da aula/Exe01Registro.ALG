Algoritmo "semnome"
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2024

tipo
conta=registro
   numero: inteiro
   nome: caractere
   saldo: real
fimregistro
Var
// Se��o de Declara��es das vari�veis 
r: conta

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
r.numero <- 111000
r.nome <- "Pablo Mar�al"
r.saldo <- 2500000000000

// Mostrando os dados
 escreval("Nome: ", r.nome)
 escreval("Numero: ", r.numero)
 escreval("Saldo: ", r.saldo)

Fimalgoritmo