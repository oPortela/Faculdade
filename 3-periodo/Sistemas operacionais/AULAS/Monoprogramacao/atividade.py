import time

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class MonoProgrammingSimulator:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task):
        self.task_queue.append(task)

    def run(self):
        while self.task_queue:
            current_task = self.task_queue.pop(0)
            print(f"Executando a tarefa: {current_task.name}")
            time.sleep(current_task.duration)
            print(f"Tarefa {current_task.name} concluída!")

# Exemplo de uso
simulator = MonoProgrammingSimulator()
simulator.add_task(Task("Tarefa 1", 2))
simulator.add_task(Task("Tarefa 2", 3))
simulator.add_task(Task("Tarefa 3", 1))
simulator.run()
