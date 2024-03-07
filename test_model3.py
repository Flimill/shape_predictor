import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def test_model(name, class_names, test_path, img_width, img_height):
    # Загружаем модель
    model = load_model(name)

    # Создаем генератор данных
    datagen = ImageDataGenerator(rescale=1./255)

    # Генерируем данные из директории
    generator = datagen.flow_from_directory(
        test_path,
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode='categorical',
        classes=class_names,
        shuffle=False
    )

    # Делаем предсказание
    predictions = model.predict(generator, steps=len(generator), verbose=1)
    predicted_classes = np.argmax(predictions, axis=1)

    # Получаем истинные метки
    true_labels = generator.classes

    # Вычисляем точность
    accuracy = np.mean(predicted_classes == true_labels)

    print(f'Accuracy: {accuracy * 100:.2f}%')
    return accuracy




# Пример вызова функции
#test_model('models/shape_predictor5.h5', ['boxes', 'circles', 'treangle'], 'testing_dataset',64,64)
