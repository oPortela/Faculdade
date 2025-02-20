#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles. o Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#o necessita da esfera;
#o necessita de limpeza; 
#necessita troca do cabo ou conector; 
#quebrado ou inutilizado
#Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

def percentual(numerosMouses, qtd_mouse):
    return (numerosMouses / qtd_mouse) * 100 if qtd_mouse > 0 else 0

tipoDefeito = [
    'Necessita de esfera', 
    'Necessita de limpeza', 
    'Necessita troca do cabo ou conector', 
    'Quebrado ou inutilizado'
    ]

numerosMouses = [0] * len(tipoDefeito)

numeroDefeito = 1

print('----------------- Bem vindo ao sistema de controle e manutenção -----------------\n')
for i in range(len(tipoDefeito)):
    print(f'{i + 1}- {tipoDefeito[i]}')
    
    if i == (len(tipoDefeito) - 1):
        print('\n')
    
while True:
    numeroDefeito = int(input('Digite qual o defeito do mouse (0 para sair do sistema): '))
    
    if numeroDefeito == 0:
        break
    elif 1 <= numeroDefeito <= len(tipoDefeito):
        numerosMouses[numeroDefeito - 1] += 1 #adiciona um mouse ao defeito
    else:
        print('Número inválido!')
       
qtd_mouse = sum(numerosMouses) 
print(f'Quantidade de mouses: {qtd_mouse}')

#Relatorio final
#print(f'\nSituação{:<40}Quantidade{:<19}Percentual')
for i in range(len(tipoDefeito)):
    print(f'{tipoDefeito[i]:<40} {numerosMouses[i]:<19} {percentual(numerosMouses[i], qtd_mouse):.2f}%')