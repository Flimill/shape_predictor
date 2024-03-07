import os
import random
from generate_photo import genererate_pictures
from test_model4 import test_model
from train_model import train_model
from plot_graph import plot_graph_layers, plot_graph_neurons

test_accuracy = 0.0
models_number = 0

activation_array = ['relu', 'sigmoid', 'tanh', 'softmax','leaky_relu']

for activation in activation_array:
    num_layers_array = []
    accuracy_array = []
    num_neurons_array = []
    
    for num_layers in range(1,15):
        models_number+=1
        
        #пути к данным
        train_ds_path = 'training_dataset' 
        test_ds_path = 'testing_dataset' 
        models_path = 'models'  
        
        #генерация новызх картинок
        img_width=64
        img_height=64
        num_samples_train= 5000#random.randint(4000, 5000)
        num_samples_test=1000
        min_fig_size = 10
        class_names = ['boxes', 'circles', 'treangle'] 
        #genererate_pictures(train_ds_path,num_samples_train,img_width,img_height,min_fig_size)
        #genererate_pictures(test_ds_path, num_samples_test,img_width,img_height,min_fig_size)
        
        #тренировка модели
        num_classes = 3  # всего классов
        epochs = 20#random.randint(17, 25)  # Количество эпох
        batch_size = 64  # Размер мини-выборки
        learning_rate = 0.001#random.choice([0.01,0.001])
        num_layers = models_number
        name, num_neurons = train_model(train_ds_path,models_path,num_classes,epochs,batch_size,img_height, img_width,models_number,learning_rate, num_layers, activation)
        
        #тестирование модели
        test_accuracy3 = test_model(name, class_names, test_ds_path, img_width, img_height)
        num_layers_array.append(num_layers)
        accuracy_array.append(test_accuracy3)
        num_neurons_array.append(num_neurons)
        print(num_layers_array)
        print(accuracy_array)
        print(num_neurons_array)
        print(f'num_layers_array = {num_layers}')
        print(f'num_neurons = {num_neurons}')
        print(f'test_accuracy3 = {test_accuracy3}')   
        print(num_samples_train)
        print(epochs)
        print(batch_size)
        print(learning_rate)
        print(models_number)
        
        
    #Строим графики
    plot_graph_layers(num_layers_array, accuracy_array, activation)
    plot_graph_neurons(accuracy_array, num_neurons_array, activation)
    



    