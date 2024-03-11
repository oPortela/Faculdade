import threading

# Dicionário para armazenar os saldos das contas
saldos = {"Conta A": 1000, "Conta B": 1500}
semaforo = threading.Semaphore()

# Função para transferência bancária
def transferencia_bancaria(valor, conta_origem, conta_destino):
    global saldos

    # Bloqueia o acesso aos saldos das contas
    semaforo.acquire()

    try:
        if saldos[conta_origem] >= valor:
            saldos[conta_origem] -= valor
            saldos[conta_destino] += valor
            print(f"Transferência de R${valor:.2f} da {conta_origem} para {conta_destino}.")
            print(f"Saldo da {conta_origem}: R${saldos[conta_origem]:.2f}")
            print(f"Saldo da {conta_destino}: R${saldos[conta_destino]:.2f}")
        else:
            print(f"Saldo insuficiente na {conta_origem}.")
    finally:
        # Libera o semáforo
        semaforo.release()

def main():
    while True:
        # Criação de threads para transferências
        valor1 = int(input('Digite o valor da transferencia da Conta A para a Conta B: '))
        valor2 = int(input('Digite o valor da transferencia da Conta B para a Conta A: '))
        
        thread1 = threading.Thread(target=transferencia_bancaria, args=(valor1, "Conta A", "Conta B"))
        thread2 = threading.Thread(target=transferencia_bancaria, args=(valor2, "Conta B", "Conta A"))

        # Inicia as threads
        thread1.start()
        thread2.start()

        # Espera até que ambas as threads terminem
        thread1.join()
        thread2.join()

        op = input('Deseja realizar outra transferência: (S para sim ou clica qualquer tecla para sair) ').upper()
        
        if op != 'S':
            print('Até a proxima.')
            break
         
        print(f"Saldo final da Conta A: R${saldos['Conta A']:.2f}")
        print(f"Saldo final da Conta B: R${saldos['Conta B']:.2f}")


main()