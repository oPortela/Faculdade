#Atividade 07

def media(nota1, nota2, nota3, tipoMedia):
    match tipoMedia:
        case 'A': #Média aritmética
            media = (nota1 + nota2 + nota3) / 3
            return media
        case 'P': #Média ponderada
            peso1 = 5
            peso2 = 3
            peso3 = 2
            
            media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
            return media
        case _:
            return print('Opção inválida')
            
def main():
    print('Bem vindo ao sistemas de notas')    
    
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))       
    n3 = float(input('Digite a terceira nota: '))  
    opcao = input('Qual opção de média deseja calcular: (P para ponderada) e (A para aritmética) ').upper() 
    
    mediaNotas = media(n1, n2, n3, opcao)  
    
    print(f'A média nos números é {mediaNotas:.2f}')        

main()