# alleen voor testdoeleinden

import warnings
import os
import numpy as np

warnings.simplefilter("ignore")
import keras_tuner as kt
import keras
import tensorflow as tf


fn_tfmodel = r"C:\Users\marcr\MakeAIWork\simpylc\tensorflow\test_tf2_v1"

path_input = r"C:\Users\marcr\MakeAIWork\simpylc\simulations\car\control_client"
sonar_input = "sonar.samples_v1"
sonar_array = np.genfromtxt(os.path.join(path_input, sonar_input))

i = sonar_array.shape[0] // 10
sonardata = sonar_array[:-i, 0:3]  # Dit is de input.
steeringdata = sonar_array[:-i, 3]  # Dit komt overeen met het label/output
sonardata_val = sonar_array[-i:, 0:3]  # Dit is de input.
steeringdata_val = sonar_array[-i:, 3]  # Dit komt overeen met het label/output

# tfmodel = tf.keras.models.load_model(fn_tfmodel)


def model_builder(hp):
    hp_units = hp.Int("units", min_value=2, max_value=30, step=4)

    # model.add(keras.layers.Dense(units=hp_units, activation="relu"))
    # Tune the number of units in the first Dense layer
    # Choose an optimal value between 32-512
    # model.add(keras.layers.Dense(10))
    # model = keras.Sequential()
    # model.add(keras.layers.Flatten(input_shape=(28, 28)))
    model = tf.keras.Sequential(
        [
            # tf.keras.layers.Flatten(input_shape=([3]), # input laag.
            tf.keras.Input(shape=(3,)),  # input laag.
            tf.keras.layers.Dense(12, activation="relu"),  # 1e hidden layer
            # tf.keras.layers.Dense(units=hp_units, activation="relu"),  # 1e hidden layer
            tf.keras.layers.Dense(units=hp_units, activation="relu"),  # 1e hidden layer
            # tf.keras.layers.Dense(units=hp_units, activation="relu"),  # 1e hidden layer
            # tf.keras.layers.Dense(units=hp_units, activation="relu"),  # 1e hidden layer
            # tf.keras.layers.Dense(units=hp_units, activation="relu"),  # 1e hidden layer
            # tf.keras.layers.Dense(2, activation='relu'),  # 2e hidden layer
            tf.keras.layers.Dense(1),
        ]
    )  # output layer

    # Tune the learning rate for the optimizer
    # Choose an optimal value from 0.01, 0.001, or 0.0001

    hp_learning_rate = hp.Choice("learning_rate", values=[1e-2, 1e-3, 1e-4])
    lf = tf.keras.losses.mean_squared_error
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate),
        loss=lf,
        metrics=["mae"],
    )
    # model.compile(optimizer=optimizer,
    #        loss=lf,
    #        metrics=['accuracy'])
    return model


# tuner = kt.Hyperband(tfmodel,
tuner = kt.Hyperband(
    model_builder,
    objective="val_mae",
    # objective='val_xxx',
    max_epochs=50,
    factor=3,
    directory="my_dir7",
    project_name="intro_to_kt",
)

stop_early = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=5)

tuner.search(
    sonardata, steeringdata, epochs=50, validation_split=0.2, callbacks=[stop_early]
)
best_hps = tuner.get_best_hyperparameters(num_trials=3)[0]
print(best_hps)

print(
    f"""
The hyperparameter search is complete. The optimal number of units in the first densely-connected
layer is {best_hps.get('units')} and the optimal learning rate for the optimizer
is {best_hps.get('learning_rate')}.
"""
)
