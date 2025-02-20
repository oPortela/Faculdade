import threading
import queue
import time

# Cria uma fila para os processos
process_queue = queue.Queue()

# Define a duração do quantum
quantum = 2

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
    Se o processo não terminar dentro do quantum, ele é colocado de volta na fila.
    """
    while not process_queue.empty():
        # Pega o próximo processo da fila
        id, duration = process_queue.get()
        if duration > quantum:
            # Se o processo não terminar dentro do quantum, ele é colocado de volta na fila
            threading.Thread(target=process, args=(id, quantum)).start()
            process_queue.put((id, duration - quantum))
        else:
            threading.Thread(target=process, args=(id, duration)).start()

if __name__ == "__main__":
    # Adiciona alguns processos à fila
    n1 = 0
    while True:
        n1 += 1
        for i in range(n1):
            process_queue.put((i, 5)) # cada processo tem duração 5

            # Inicia o escalonador
            scheduler()
