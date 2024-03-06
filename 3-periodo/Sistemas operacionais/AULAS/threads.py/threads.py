import threading
import time

#Recurso a ser consumido
recurso_disponivel = False
cv = threading.Condition() #Controla a execução das threads

#Metodo que produz os recursos que serão consumidos
def produtor():
    global recurso_disponivel
    while True:
        with cv:
            recurso_disponivel = True
            print('Produtor: Recurso produzido!')
            cv.notify_all()
        #Tempo de espera para o proximo recursp
        time.sleep(1)
        
def consumidor(id):
    global recurso_disponivel
    while True:
        with  cv:
            while not recurso_disponivel:
                cv.wait() #Espera pelo recurso
            print("Consumidor ", id, " Recurso produzido")
            recurso_disponivel = False
            #Aguarda um tempo de consumir novamente
            time.sleep(0.5)

#Execução do processo e criação de threads
def main():
    #Cria threads
    t1 =threading.Thread(target=produtor) #Thread do produtor
    t2 = threading.Thread(target=consumidor, args=(1,)) #consumidor
    t3 = threading.Thread(target=consumidor, args=(2,)) #consumidor
    #Inicia as threads
    t1.start()
    t2.start()
    t3.start()
    #Colocanco as threads em funcionamento
    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
    

def main2():
    num_consumidores = int(input("Quantos consumidores deseja iniciar?"))
    t1 = threading.Thread(target=produtor) 
    t1.start() 

    threads_consumidor = []
    for i in range(num_consumidores):
        t = threading.Thread(target=consumidor, args=(i+1,))
        threads_consumidor.append(t)
        t.start()

    t1.join()
    for t in threads_consumidor:
        t.join()

#if __name__ == "__main__":
 #   main2()