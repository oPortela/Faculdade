Algoritmo "exe02_Registro"

// Criando uma variável do tipo registro
tipo
passagem=registro
  numeroPassagem: inteiro
  data: caracter
  origem: caracter
  destino:caracter
  horario: caracter
  poltrona: inteiro
  idade: inteiro
  nomePassageiro: caracter
fimregistro
Var
// Seção de Declarações das variáveis 
vp: vetor[0..2] de passagem
i: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
// Inserindo dados no vetor de registro
para i de 1 ate 2 passo 1 faca
     escreval("Digite o Numero da Passagem: ")
     leia(vp.numeroPassagem[i])
     escreval("Dada da Passagem: ")
     leia(vp.data[i])
     escreval("Origem da Viagem: ")
     leia(vp.origem[i])
     escreval("Destino da Viagem: ")
     leia(vp.destino[i])
     escreval("Horário de Saída: ")
     leia(vp.horario[i])
     escreval("Numero da Poltrona: ")
     leia(vp.poltrona[i])
     escreval("Idade do Passageiro: ")
     leia(vp.idade[i])
     escreval("Nome do Passageiro: ")
     leia(vp.nomePassageiro[i])
     escreval()
fimpara

// Mostrando os dados que foram armazenados
para i de 1 ate 2 passo 1 faca
     escreval("Dados Amazenados no Indice ", i, "do Vetor de Registro.")
     escreval("-------------------------------------------------------")
     escreval("Passageiro: ",vp.nomePassageiro[i], " - Idade: ", vp.idade[i])
     escreval("Numero Passagem: ",vp.numeroPassagem[i], "-- Pontrona: ",vp.poltrona[i])
     escreval("Origem: ",vp.origem[i], "  -- Destino: ",vp.destino[i])
     escreval("Data Viagem: ",vp.data[i])
     escreval()
fimpara
     
Fimalgoritmo