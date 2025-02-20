Funcionario = []

for i in range(2):
    funcionario = {} #criando o registro vazio
    funcionario['nome'] = input("Digite o nome do funcionario")
    funcionario['salario'] = float(input(f"Digite o salario do \
                                         funcionario {funcionario['nome']}: "))
    Funcionario.append(funcionario)

#imprimindo o vetor de registro
for i in range(2):
    print(f"Funcionario que ocupa a posição[{i}] no vetor: ")
    print(f"Nome: {Funcionario[i]['nome']} ")
    print(f"Salário: R$ {Funcionario[i]['salario']:.2f}")