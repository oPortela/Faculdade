import matplotlib.pyplot as plt
import numpy as np

def plot_funcao(expressao, intervalo_x, delta):
    # Avalia a expressão matemática em um intervalo de x
    x = np.arange(intervalo_x[0], intervalo_x[1], delta)
    y = eval(expressao)

    # Cria o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=expressao)
    plt.title("Gráfico da Função")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.legend()
    plt.grid(True)
    
    plt.show()

# Exemplo de uso:
expressao = "x**2 + 3*x - 5"
intervalo_x = (-10, 10)  # Intervalo de x
delta = 0.1  # Espaçamento entre os valores de x

plot_funcao(expressao, intervalo_x, delta)
