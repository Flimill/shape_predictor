from os.path import join
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling
from os.path import exists
from os import makedirs
from keras.optimizers import Adam, SGD


def train_model(train_ds_path,models_path,num_classes,epochs,batch_size,img_height, img_width,models_number,learning_rate, num_layers, activation,momentum=0):
    data_dir = join(train_ds_path) #каталог с данными
    input_shape = (img_height, img_width, 3)  # размерность картинки
    #выбираем оптимизатор
    #optimizer = SGD(learning_rate=learning_rate, momentum=momentum)
    optimizer=Adam(learning_rate=learning_rate)

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
    model.add(Rescaling(1./255))  # Нормализация
    model.add(Flatten(input_shape=(input_shape)))
    for i in range(num_layers):
        model.add(Dense(128, activation=activation))
    model.add(Dense(num_classes, activation='softmax')) 


    # Компилируем модель
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])


    # Обучаем модель
    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs,
    )
    # Сохраняем модель
    if not exists(models_path): makedirs(models_path)
    num_neurons = sum(layer.units for layer in model.layers if isinstance(layer, Dense))
    name = f'{models_path}/shape_predictor{models_number}.h5'
    model.save(name)
    return name, num_neurons
