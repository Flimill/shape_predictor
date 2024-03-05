from os.path import join
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
from os.path import exists
from os import makedirs
from tensorflow.keras.optimizers import Adam


def train_model(train_path,models_path,num_classes,epochs,batch_size,img_height, img_width,models_number,learning_rate):
    data_dir = join(train_path) #каталог с данными
    input_shape = (img_height, img_width, 3)  # размерность картинки
    # Инициализируем генератор изображений
    train_ds = keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        # shuffle=False,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    val_ds = keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        # shuffle=False,
        image_size=(img_height, img_width),
        batch_size=batch_size)
    # Создаем модель
    model = Sequential()

    # Добавляем сверточные слои
    model.add(Input(shape=input_shape))
    model.add(Conv2D(1, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(2, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(4, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Преобразуем данные в один вектор
    model.add(Flatten())

    # Добавляем полносвязные слои
    model.add(Dense(128, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))  # 3 класса: круг, ромб, квадрат

    # Компилируем модель
    model.compile(optimizer=Adam(learning_rate=learning_rate), loss='sparse_categorical_crossentropy', metrics=['accuracy'])


    # Обучаем модель
    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs,
    )
    # Сохраняем модель
    if not exists(models_path): makedirs(models_path)
    name = f'{models_path}/shape_predictor{models_number}.h5'
    model.save(name)
    return name
