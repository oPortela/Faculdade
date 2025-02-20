import time
import subprocess

#Classe que cria as tarefas do sistema

class Task:
    def __init__(self, name, duration):
        self.name = name #nome do processo
        self.duration = duration #Tempo de execução

#Classe que simula o SO Monoprogramado
class MonoProgramingSimulator:
    def __init__(self):
        self.task_queue = [] #Cria a fila vazia
        
    #Metodo que adiciona processo na fila de execução
    def add_task(self, task):
        self.task_queue.append(task)
    
    #Metodo que executa a simulação do SO
    def run(self):
        while self.task_queue:
            #Recebe tarefa em execução e retira da fila
            current_task = self.task_queue.pop(0)
            print(f'Executando a tarefa: {current_task.name}')
            #Implementa o tempo de execução da tarefa
            time.sleep(current_task.duration)
            print(f'Tarefa {current_task.name} concluída!')

#execução da simulação

chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
anydesk = 'C:\Program Files (x86)\AnyDesk\AnyDesk.exe'
edge = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
calc = 'calc.exe'
virtual = 'C:\Program Files\Oracle\VirtualBox\VirtualBox.exe'
team = 'C:\Program Files\TeamViewer\TeamViewer.exe'
player = 'E:\LDPlayer\LDPlayer9\dnplayer.exe'
explorer = 'C:\Windows\explorer.exe'
wordpad = 'C:\Windows\write.exe'
jogo = 'E:\HorizonChaseTurbo\HorizonChase.exe'


simulator = MonoProgramingSimulator()

simulator.add_task(Task(subprocess.Popen(team), 5))
simulator.add_task(Task(subprocess.Popen(anydesk), 3))
simulator.add_task(Task(subprocess.Popen(edge), 7))
simulator.add_task(Task(subprocess.Popen(chrome), 2))
simulator.add_task(Task(subprocess.Popen(calc), 2))
simulator.add_task(Task(subprocess.Popen(virtual), 2))
simulator.add_task(Task(subprocess.Popen(player), 2))
simulator.add_task(Task(subprocess.Popen(explorer), 2))
simulator.add_task(Task(subprocess.Popen(wordpad), 2))
simulator.add_task(Task(subprocess.Popen(jogo), 2))

simulator.run()