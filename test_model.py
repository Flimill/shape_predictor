from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

def test_model(name, class_names, test_path):
    # Загружаем модель
    model = load_model(name)

    # Путь к папке с тестовыми изображениями
    test_data_path = test_path

    # Список для хранения предсказаний
    predictions = []

    # Список для хранения истинных меток
    true_labels = []

    # Перебираем все директории в папке с тестовыми данными
    for folder_name in os.listdir(test_data_path):
        folder_path = os.path.join(test_data_path, folder_name)
        if os.path.isdir(folder_path):
            # Перебираем все файлы в директории
            for filename in os.listdir(folder_path):
                img_path = os.path.join(folder_path, filename)
                if os.path.isfile(img_path):
                    # Загружаем изображение
                    img = image.load_img(img_path, target_size=(64, 64))
                    img_array = image.img_to_array(img)
                    img_array = np.expand_dims(img_array, axis=0)
                    img_array /= 255.

                    # Делаем предсказание
                    prediction = model.predict(img_array)
                    predicted_class = np.argmax(prediction)

                    # Добавляем предсказание и истинную метку в списки
                    predictions.append(predicted_class)
                    true_labels.append(folder_name)

    # Преобразуем метки в числовые значения

    true_labels_numeric = [class_names.index(label) for label in true_labels]

    # Вычисляем точность
    accuracy = np.mean(np.array(predictions) == np.array(true_labels_numeric))

    print(f'Accuracy: {accuracy * 100:.2f}%')
    return accuracy

#print(test_model('models/shape_predictor1.h5', ['boxes', 'circles', 'treangle'],'testing_dataset' ))