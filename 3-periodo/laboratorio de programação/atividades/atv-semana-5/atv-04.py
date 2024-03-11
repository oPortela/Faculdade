def tempo(segundo):
    hora = segundo // 3600
    segundos_restantes = segundo % 3600
    minuto = segundos_restantes // 60
    segundos = segundos_restantes % 60

    return hora, minuto, segundos
    
def main():
    seg = int(input('Digite o valor de segundos: '))
    
    horas, minutos, segundos = tempo(seg)
    
    print(f'O valor de {seg} segundos tem {horas} horas, {minutos} minutos e {segundos} segundos.')
    
main()
