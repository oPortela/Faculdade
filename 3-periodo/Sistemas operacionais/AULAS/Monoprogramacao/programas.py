import os
import time
import subprocess

class Task:
    def __init__(self, name, command):
        self.name = name
        self.command = command

class MonoProgrammingSimulator:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task):
        self.task_queue.append(task)

    def run(self):
        while self.task_queue:
            current_task = self.task_queue.pop(0)
            print(f"Executando a tarefa: {current_task.name}")
            subprocess.call(current_task.command, shell=True)
            print(f"Tarefa {current_task.name} concluída!")

# Exemplo de uso
simulator = MonoProgrammingSimulator()
simulator.add_task(Task("Abrir Microsoft Edge", "start msedge"))
simulator.add_task(Task("Abrir Bloco de Notas", "start notepad"))
simulator.run()
