import tensorflow as tf

# Загрузка модели из файла .h5
model = tf.keras.models.load_model('final_models/88.67%/shape_predictor24.h5')

# Получение весов каждого слоя
for layer in model.layers:
    print("Layer Name:", layer.name)
    print("Weights:", layer.get_weights())
    print("\n")
