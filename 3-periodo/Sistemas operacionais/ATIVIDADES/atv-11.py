import threading
import random
import time
import sys

class ResourceManager:
    def __init__(self, numeroRecursos):
        self.numeroRecursos = numeroRecursos
        self.avaliacaoRecursos = [threading.Lock() for _ in range(numeroRecursos)]
        self.lock = threading.Lock()

    def request_resource(self):
        while True:
            id_recursos = random.randint(0, self.numeroRecursos - 1)
            if self.avaliacaoRecursos[id_recursos].acquire(blocking=False):
                return id_recursos

    def release_resource(self, id_recursos):
        self.avaliacaoRecursos[id_recursos].release()

def thread_function(thread_id, gerenciadorRecursos, finalizarEvento):
    print(f"Thread {thread_id} iniciada")
    while not finalizarEvento.is_set():
        try:
            time.sleep(random.uniform(0.5, 2.0)) 
            print(f"Thread {thread_id} está solicitando um recurso")
            id_recursos = gerenciadorRecursos.request_resource()
            print(f"Thread {thread_id} obteve o recurso {id_recursos}")
            time.sleep(random.uniform(0.5, 2.0))
            print(f"Thread {thread_id} está liberando o recurso {id_recursos}")
            gerenciadorRecursos.release_resource(id_recursos)
        except KeyboardInterrupt:
            finalizarEvento.set()

def main(numeroThreads, numeroRecursos):
    gerenciadorRecursos = ResourceManager(numeroRecursos)
    threads = []
    finalizarEvento = threading.Event()

    for i in range(numeroThreads):
        thread = threading.Thread(target=thread_function, args=(i, gerenciadorRecursos, finalizarEvento))
        threads.append(thread)
        thread.start()

    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("Encerrando...")
        finalizarEvento.set()
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    try:
        numeroThreads = int(input("Digite o número de threads: "))
        numeroRecursos = int(input("Digite o número de recursos: "))
        main(numeroThreads, numeroRecursos)
    except ValueError:
        print("Por favor, insira um número válido para o número de threads e recursos.")
        sys.exit(1)
