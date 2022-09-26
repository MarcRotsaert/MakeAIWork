import tensorflow as tf
import numpy as np
import os

path_input = r'C:\Users\marcr\MakeAIWork\simpylc\simulations\car\control_client'
sonar_input = 'sonar.samples'
sonar_array = np.genfromtxt(os.path.join(path_input,sonar_input))

#10 procent reserveren voor validatie
i = sonar_array.shape[0]//10
sonardata =    sonar_array[:-i,0:3] # Dit is de input.
steeringdata = sonar_array[:-i,3] # Dit komt overeen met het label/output
sonardata_val =    sonar_array[-i:,0:3] # Dit is de input.
steeringdata_val = sonar_array[-i:,3] # Dit komt overeen met het label/output


nrepochs = 30

"""
Neuraal netwerk bestaat uit
    3 input-nodes.
    1 output node.
De sonardata krijgt als label de sturingshoek.

"""
print('\n')


def fittester(lf,optimizer,epochs):
    #test 
    model = tf.keras.Sequential([
    #tf.keras.layers.Flatten(input_shape=([3]), # input laag.
        tf.keras.Input(shape=(3,)), # input laag.
        tf.keras.layers.Dense(24, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(12, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(6, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(1)])              # output layer

    model.compile(optimizer=optimizer, 
            loss=lf,
            metrics=['accuracy'])

    #x=(sonardata-sonardata.min())/(sonardata.max()-sonardata.min())
    history=model.fit(sonardata,steeringdata,epochs=nrepochs,verbose=0)
    print(history.history['accuracy']   )
    results=model.evaluate(sonardata_val,steeringdata_val)
    print('loss: ' + str(results[0]),'accuracy: ' + str(results[1]) )
    sw_prediction= model.predict(sonardata_val)
    print([sw_prediction.min(),sw_prediction.mean(),sw_prediction.max()])
    
    print('_____________________________\n')
    #model.fit(sonardata,steeringdata,epochs=5)

if False:
    #tensorflow-model opzet.
    lossf = [tf.keras.losses.mean_squared_error,
        tf.keras.losses.kl_divergence,
        tf.keras.losses.mean_absolute_error,
        tf.keras.losses.mean_absolute_percentage_error,
        tf.keras.losses.binary_crossentropy,
        tf.keras.losses.categorical_crossentropy,
    ]

    optmzr ='adam'
    for lf in lossf:
        print(lf)
        fittester(lf,optmzr,nrepochs)

if False:
    optimizers = [ 'adam','rmsprop','sgd']
    #optimizers = [ 'sgd']
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        print(optmzr)
        fittester(lf,optmzr,nrepochs)
        #De code hieronder snap ik nog niet echt. 

if True:
    optimizers = [ 'adam',]
    #optimizers = [ 'sgd']
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        fittester(lf,optmzr,nrepochs)

