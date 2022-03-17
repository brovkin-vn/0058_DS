import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Model, Sequential, layers
import numpy as np

input = keras.Input(shape=(1000,))
output = input
for _ in range(4):
    output = layers.Concatenate()([output, layers.Dense(1000, 'relu')(output)])
model = Model(inputs=input, outputs=output)
model.summary()