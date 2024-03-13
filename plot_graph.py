import time
import matplotlib.pyplot as plt

def save_graph(array, accuracy_array, activation,learning_rate, array_name, num):
    filename = f'{array_name}_{activation}_{learning_rate}_{num}.png'
    time.sleep(1)
# Создаем новое окно для графика
    plt.figure()

    #positions = list(range(len(array)))


    # Строим график, используя позиции в качестве абсцисс
    plt.plot(array, accuracy_array, marker='o')

    # Устанавливаем метки на оси абсцисс с использованием значений из array
    #plt.xticks(positions, array)
    
    plt.title(f'Зависимость accuracy от {array_name}, для передаточной функции {activation}')
    plt.xlabel(array_name)
    plt.ylabel('Точность (accuracy)')
    plt.grid(True)
    plt.savefig(filename) # Сохраняем график в файл
    plt.close() # Закрываем окно графика