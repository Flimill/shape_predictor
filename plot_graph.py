import time
import matplotlib.pyplot as plt


def plot_graph_layers(num_layers_array, accuracy_array, activation):
    # Построение графика точности от числа слоев
    plt.figure()  # Создаем новое окно для графика
    plt.plot(num_layers_array, accuracy_array, marker='o')
    plt.title(f'Зависимость точности от числа слоев, для передаточной функции {activation}')
    plt.xlabel('Число слоев')
    plt.ylabel('Точность (accuracy)')
    plt.grid(True)
    plt.show(block=False)
    plt.pause(5)

def plot_graph_neurons(accuracy_array, num_neurons, activation):
    time.sleep(5)    
    # Создаем новое окно для графика
    plt.figure()
    
    # Построение графика точности от числа нейронов
    plt.plot(num_neurons, accuracy_array, marker='o')
    plt.title(f'Зависимость точности от числа нейронов, для передаточной функции {activation}')
    plt.xlabel('Число слоев')
    plt.ylabel('Точность (accuracy)')
    plt.grid(True)
    plt.show(block=False)
    plt.pause(5)