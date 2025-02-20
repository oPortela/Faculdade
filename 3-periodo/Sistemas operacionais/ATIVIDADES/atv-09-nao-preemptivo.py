import queue
import time

# Cria uma fila para os processos
process_queue = queue.Queue()

def process(id, duration):
    """
    Função que simula um processo.
    Cada processo "dorme" por um tempo para simular a execução.
    
    """
    print(f'Processo {id} iniciado, duração {duration}')
    for _ in range(duration):
        time.sleep(1) # simula a execução do processo
        print(f'Processo {id} executando')
    print(f'Processo {id} finalizado')

def scheduler():
    """
    Função que simula o escalonador de processos.
    O escalonador pega o próximo processo da fila e inicia a execução.
    """
    while not process_queue.empty():
        # Pega o próximo processo da fila
        id, duration = process_queue.get()
        process(id, duration)

if __name__ == "__main__":
    # Adiciona alguns processos à fila
    n1 = 0
    while True:
        n1 += 1
        process_queue.put((n1, 5)) # cada processo tem duração 5

    # Inicia o escalonador
        scheduler()
