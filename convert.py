# Modelo de IA que convierte celsius a farenheit sin la necesidad de expresar una formula

import tensorflow as tf
import numpy as np
import time as t

# Data Train
celsius = np.array([-40,-10,0,8,15,22,38], dtype=float)
farenheit = np.array([-40,14,32,46,59,72,100], dtype=float)

# Model Creation
o1 = tf.keras.layers.Dense(units=4, input_shape=[1])
o2 = tf.keras.layers.Dense(units=4)
o3 = tf.keras.layers.Dense(units=4)
ex = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([o1,o2,o3,ex])

# Model Compilation
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

# Train
print('Entrenando...')
history = model.fit(celsius, farenheit, epochs=2000, verbose=False)
print('Entrenamiento finalizado!')

# Calculo complejo - while - comprobación
t.sleep(1)
print('\nSi desea salir escriba ex\n')

while True:
    nc = input('Ingrese el valor en CELSIUS a convertir: ')
    if nc == 'ex':
        print('Vuelva pronto!')
        t.sleep(2)
        break
    else:
        if nc.isdigit() == True:
            # Calculo
            nc = int(nc)
            print('Calculando...')
            t.sleep(1)
            re = model.predict([nc,0])
            print('El resultado es: '+str(re)+' farenheit')
        else:
            print('No has ingresado un número!')
            exit