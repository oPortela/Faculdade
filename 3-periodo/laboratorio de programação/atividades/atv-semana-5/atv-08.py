'''
Crie uma sub-rotina que receba como parâmetro a hora de início e a hora de término de um
jogo, ambas subdivididas em dois valores distintos: horas e minutos. A sub-rotina deverá
retornar a duração expressa em minutos, considerando que o tempo máximo de duração
de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.
'''

def duracaoJogo(horaInicio, minutoInicio, horaFim, minutoFim):
    if horaFim < horaInicio:
        duracaoHoras = (24 - horaInicio) + horaFim
    else:
        duracaoHoras = horaFim - horaInicio
        
    if minutoFim < minutoInicio:     
        duracaoMinutos = (60 - minutoInicio) + minutoFim
        duracaoHoras -= 1  # Reduzir uma hora se os minutos de término forem menores que os minutos de início
    else:
        duracaoMinutos = minutoFim - minutoInicio
    
    tempoMinutos = (duracaoHoras * 60) + duracaoMinutos
    
    return tempoMinutos

def main():
    print('Bem vindo ao sistema de calculo de duração de provas')
    
    horaIni = int(input('Digite a hora de Inicio da prova: '))
    minutoIni = int(input('Digite os minutos de Inicio da prova: '))
    horaFim = int(input('Digite a hora de término da prova: '))
    minutoFim = int(input('Digite os minutos de término da prova: '))
    
    duracao = duracaoJogo(horaIni, minutoIni, horaFim, minutoFim)
    
    if horaFim < horaIni:
        dia = 'outro dia' 
    else: 
        dia = 'mesmo dia'
    
    print(f'A prova realizada teve início às {horaIni}:{minutoIni} e terminou no {dia} às {horaFim}:{minutoFim}. Esta prova teve a duração de {duracao} minutos.')

main()
