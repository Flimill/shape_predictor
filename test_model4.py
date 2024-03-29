import numpy as np
from keras.models import load_model
import tensorflow as tf
from tensorflow import keras

def test_model(name, class_names, test_path, img_width, img_height):
    # Загружаем модель
    model = load_model(name)

    # Генерируем данные из директории
    generator = keras.utils.image_dataset_from_directory(
        test_path,
        image_size=(img_width, img_height),
        batch_size=64,
        shuffle=False
    )

    # Делаем предсказание
    predictions = model.predict(generator, steps=len(generator), verbose=1)
    predicted_classes = np.argmax(predictions, axis=1)

    # Получаем истинные метки
    true_labels = []
    for images, labels in generator:
        true_labels.extend(labels.numpy())

    # Вычисляем точность
    accuracy = np.mean(predicted_classes == true_labels)

    print(f'Accuracy: {accuracy * 100:.2f}%')
    return accuracy

# Пример вызова функции
#test_model('final_models/98.53%/shape_predictor24.h5', ['boxes', 'circles', 'treangle'], 'testing_dataset', 64, 64)