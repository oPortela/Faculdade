def calcular_percentual(numeros_mouses, qtd_mouse):
    return (numeros_mouses / qtd_mouse) * 100 if qtd_mouse > 0 else 0

tipo_defeito = [
    'Necessita de esfera', 
    'Necessita de limpeza', 
    'Necessita troca do cabo ou conector', 
    'Quebrado ou inutilizado'
]

numeros_mouses = [0] * len(tipo_defeito)

numero_defeito = 1

print('----------------- Bem vindo ao sistema de controle e manutenção -----------------\n')
for i in range(len(tipo_defeito)):
    print(f'{i + 1}- {tipo_defeito[i]}')
    
    if i == (len(tipo_defeito) - 1):
        print('\n')
    
while True:
    numero_defeito = int(input('Digite qual o defeito do mouse (0 para sair do sistema): '))
    
    if numero_defeito == 0:
        break
    elif 1 <= numero_defeito <= len(tipo_defeito):
        numeros_mouses[numero_defeito - 1] += 1  # Adiciona um mouse ao defeito
    else:
        print('Número inválido!')

qtd_mouse = sum(numeros_mouses) 
print(f'Quantidade de mouses: {qtd_mouse}')

# Relatorio final
# Relatorio final
print(f'\nSituação\tQuantidade\tPercentual')
for i in range(len(tipo_defeito)):
    print(f'{tipo_defeito[i]:<40} {numeros_mouses[i]:<19} {calcular_percentual(numeros_mouses[i], qtd_mouse):.2f}%')

