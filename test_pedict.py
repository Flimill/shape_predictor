import random
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

from generate_photo import draw_box_random_rotated, draw_circle_random_rotated, draw_triangle_random_rotated, random_color
w=64
h=64
min_fig_size = 10
class_names = ['boxes', 'circles', 'treangle'] 
# Загружаем модель
model = load_model('models/shape_predictor49.h5')
# Генерируем случайные изображения и делаем предсказания
num_random_images = 15  # количество случайных изображений для предсказания

# Создаем список классов

# Создаем функцию для случайной генерации изображений
def generate_random_image():
    # Выбираем случайную фигуру
    random_shape = random.choice(class_names)
    #random_shape = 'boxes'
    
    # Создаем новое изображение размером 64x64 и случайным цветом

    
    # В зависимости от выбранной фигуры, рисуем ее
    if random_shape == 'boxes':
        image = draw_box_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size)
    elif random_shape == 'circles':
        image = draw_circle_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size)
    else:
        image = draw_triangle_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size)
    
    return image


print("Предсказания для случайных изображений:")

for i in range(num_random_images):
    # Генерируем случайное изображение
    random_image = generate_random_image()
    
    # Преобразуем изображение в массив numpy и нормализуем
    img_array = image.img_to_array(random_image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.

    # Делаем предсказание
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_names[predicted_class_index]
    
    # Выводим предсказание в консоль
    print(f"Изображение {i+1}: {predicted_class}")
    
    # Показываем изображение (опционально)
    random_image.show()
    #time.sleep(3)