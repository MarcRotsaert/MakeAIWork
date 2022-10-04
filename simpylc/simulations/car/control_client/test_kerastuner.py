import warnings

warnings.simplefilter("ignore")
import keras_tuner as kt
import keras
import tensorflow as tf


fn_tfmodel = r"C:\Users\marcr\MakeAIWork\simpylc\tensorflow\test_tf2_v1"
# tfmodel = tf.keras.models.load_model(fn_tfmodel)


def model_builder(hp):
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28, 28)))

    # Tune the number of units in the first Dense layer
    # Choose an optimal value between 32-512
    hp_units = hp.Int("units", min_value=32, max_value=512, step=32)
    model.add(keras.layers.Dense(units=hp_units, activation="relu"))
    model.add(keras.layers.Dense(10))

    # Tune the learning rate for the optimizer
    # Choose an optimal value from 0.01, 0.001, or 0.0001
    hp_learning_rate = hp.Choice("learning_rate", values=[1e-2, 1e-3, 1e-4])

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate),
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )
    return model


# tuner = kt.Hyperband(tfmodel,
tuner = kt.Hyperband(
    model_builder,
    objective="val_accuracy",
    # objective='val_xxx',
    max_epochs=50,
    factor=3,
    directory="my_dir",
    project_name="intro_to_kt",
)

stop_early = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=5)

tuner.search(
    img_train, label_train, epochs=50, validation_split=0.2, callbacks=[stop_early]
)
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
