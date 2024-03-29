

import os
import random
from generate_photo import genererate_pictures
from test_model4 import test_model
from train_model import train_model

test_accuracy = 0.0
models_number = 0

while(test_accuracy < 0.95):
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
    epochs = 6#random.randint(17, 25)  # Количество эпох
    batch_size = 64  # Размер мини-выборки
    learning_rate = 0.001#random.choice([0.01,0.001])
    name = train_model(train_ds_path,models_path,num_classes,epochs,batch_size,img_height, img_width,models_number,learning_rate)
    
    #тестирование модели
    test_accuracy3 = test_model(name, class_names, test_ds_path, img_width, img_height)
    print(num_samples_train)
    print(epochs)
    print(batch_size)
    print(learning_rate)
    print(models_number)

    