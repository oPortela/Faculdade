numeroMatricula = int(input('Qual o número de sua matrícula:  '))

if numeroMatricula > 99999:
    print('o número informado ultrapassa 5 digítos, digite novamente sua matrícula.')
    numeroMatricula = int(input('Qual o número de sua matrícula:  '))

nomeCompleto = input('Qual seu nome completo: ')
genero = input('Qual o seu genêro (M(masculino) e F(feminino)):  ')
curso = input('Qual o curso que você está realizando(“BES”, “BEC” ou “ADS"):  ')
coeficiente = float(input('Qual o seu coeficiente de desempenho:  '))



if genero.upper() == 'M':
    generoC = 'Masculino'
elif genero.upper() == 'F':
    generoC = 'Feminino'
else:
    generoC = 'Indeterminado'

if curso.upper() == 'BES':
    nomeCurso = 'Bacharelado em Engenharia de Software'
elif curso.upper() == 'BEC':
    nomeCurso = 'Bacharelado em Engenharia de Computação'
elif curso.upper() == 'ADS':
    nomeCurso = 'Analise e Desenvolvimento de Sistemas'
else:
    nomeCurso = 'Curso não encontrado em nossa base de dados'

'''
if coeficiente >= 0 and coeficiente <= 100:
    if coeficiente >= 90 and coeficiente <= 100:
        coeficienteAluno = 'Excelente'
    elif coeficiente >= 70 and coeficiente < 90:
        coeficienteAluno = 'Bom'
    elif coeficiente >= 50 and coeficiente < 70:
        coeficienteAluno = 'Regular'
    elif coeficiente >= 30 and coeficiente < 50:
        coeficienteAluno = 'Necessita melhoras'
    else:
        coeficienteAluno = 'Preocupante'
else:
    print('Valor inválido!')
'''

if 0 <= coeficiente <= 100:
    if 90 <= coeficiente <= 100:
            coeficienteAluno = 'Excelente'
    elif 70 <= coeficiente < 90:
            coeficienteAluno = 'Bom'
    elif 50 <= coeficiente < 70:
            coeficienteAluno = 'Regular'
    elif 30 <= coeficiente < 50:
            coeficienteAluno = 'Necessita melhoras'
    else:
            coeficienteAluno = 'Preocupante'
else:
    coeficienteAluno = 'Valor inválido'
        


print(f'\n Nome completo: {nomeCompleto}')
print(f'O número da matrícula é: {numeroMatricula}')
print(f'Genêro: {generoC}')
print(f'Curso: {nomeCurso}')
print(f'Coeficiente de redimento: {coeficienteAluno}')