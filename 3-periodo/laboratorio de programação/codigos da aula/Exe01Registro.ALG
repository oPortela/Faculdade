Algoritmo "semnome"
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2024

tipo
conta=registro
   numero: inteiro
   nome: caractere
   saldo: real
fimregistro
Var
// Seção de Declarações das variáveis 
r: conta

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
r.numero <- 111000
r.nome <- "Pablo Marçal"
r.saldo <- 2500000000000

// Mostrando os dados
 escreval("Nome: ", r.nome)
 escreval("Numero: ", r.numero)
 escreval("Saldo: ", r.saldo)

Fimalgoritmo