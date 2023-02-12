import tensorflow as tf
import numpy as np
import time as tm
import os

# Create variables to train
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
farenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Create neuron and model
neuron = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([neuron])

# Model compile
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# Training
print("Starting training...")
historical = model.fit(celsius, farenheit, epochs=1000, verbose=False)
print("Training finished")
tm.sleep(1)

# Clear terminal
os.system('cls')

# Convertion
print("If you want to exit the programme, type the number 6609\n")
tm.sleep(2)

# While to excute always
while True:
    try:
        c_num = float(
            input("Enter the number in Celsius to be converted to Farenheit: "))
    except ValueError:
        print("\nDebes escribir un número\n")
        continue

    if (c_num == 6609):
        break

    result = model.predict([float(c_num)])
    print("The result is " + str(result) + " farenheit\n")
