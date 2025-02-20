def soma(a, b):
  sm = a + b
  return sm

def subtracao(a, b):
  sb = a - b
  return sb

def multip(a, b):
  mt = a * b
  return mt

def divisao(a, b):
  if b == 0:
    print("Não existe divisão por zero(0)")
  elif b != 0:
    dv = a / b
    return dv

def menu():
  print("*** MENU DE OPÇÃO ***")
  print(" 1 Soma: ")
  print(" 2 Subtração: ")  
  print(" 3 Multiplicação: ")  
  print(" 4 Divisão: ")  
  print(" 0 Sair do Programa: ")  

def main():
  while True:
    menu()
    op = int(input("Digite a opção Desejada: "))
    a  = int(input("Digite um valor inteiro para o cálculo desejado. "))
    b  = int(input("Digite outro valor inteiro para o cálculo desejado. "))
    
    if op == 1:
      print("** Somar Dois Valores ***")
      resp = soma(a,b)
      print(f"O Resultado da Soma é: {resp}")
    elif op == 2:
      print("** Subtrair Dois Valores ***")
      resp = subtracao(a,b)
      print(f"O Resultado da Subtração é: {resp}")
    elif op == 3:
      print("** Multiplicar Dois Valores ***")
      resp = multip(a,b)
      print(f"O Resultado da Multiplicação é: {resp}")
    elif op == 4:
      print("** Dividir Dois Valores ***")
      resp = divisao(a,b)
      print(f"O Resultado da Divisão é: {resp}")
    elif op == 0:
      print("Saindo do Programa ....")
      break
      
      
main()
      