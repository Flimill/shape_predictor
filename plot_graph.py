import time
import matplotlib.pyplot as plt


def plot_graph_layers(num_layers_array, accuracy_array, activation):
    # Построение графика точности от числа слоев
    plt.plot(num_layers_array, accuracy_array, marker='o')
    plt.title(f'Зависимость точности от числа слоев, для передаточной функции {activation}')
    plt.xlabel('Число слоев')
    plt.ylabel('Точность (accuracy)')
    plt.grid(True)
    plt.show(block=False)
    plt.pause(5) 

def plot_graph_neurons(accuracy_array, num_neurons_array, activation):    
    time.sleep(5)
    # точности от числа нейронов
    plt.plot(num_neurons_array, accuracy_array, marker='o')
    plt.title(f'Зависимость точности от числа нейронов, для предаточной функции {activation}')
    plt.xlabel('Число слоев')
    plt.ylabel('Точность (accuracy)')
    plt.grid(True)
    plt.show(block=False)
    plt.pause(5) 