from tokenize import triple_quoted
import tensorflow as tf
import numpy as np
import os

from matplotlib import pyplot as pp

path_input = r'C:\Users\marcr\MakeAIWork\simpylc\simulations\car\control_client'
lidar_input = 'lidar.samples_v1'
lidar_array = np.genfromtxt(os.path.join(path_input,lidar_input))

#10 procent reserveren voor validatie
i = lidar_array.shape[0]//10
lidardata =    lidar_array[:-i,0:16] # Dit is de input.
steeringdata = lidar_array[:-i,16] # Dit komt overeen met het label/output
lidardata_val =    lidar_array[-i:,0:16] # Dit is de input.
steeringdata_val = lidar_array[-i:,16] # Dit komt overeen met het label/output

"""
Neuraal netwerk bestaat uit
    3 input-nodes.
    1 output node.
De lidardata krijgt als label de sturingshoek.

"""
print('\n')

def fittester0(lf,optimizer,nrepochs):
    #test 
    model = tf.keras.Sequential([
    #tf.keras.layers.Flatten(input_shape=([3]), # input laag.
        tf.keras.Input(shape=(16,)), # input laag.
        tf.keras.layers.Dense(14, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(6, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(2, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(1)])              # output layer
    model = fitandtest(model)

def fittester(lf,optimizer,nrepochs):
    #test 
    model = tf.keras.Sequential([
    #tf.keras.layers.Flatten(input_shape=([3]), # input laag.
        tf.keras.Input(shape=(16,)), # input laag.
        tf.keras.layers.Dense(24, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(12, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(6, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(1)])              # output layer
    model = fitandtest(model)

def fittester2(lf,optimizer,nrepochs):
    #test 
    model = tf.keras.Sequential([
    #tf.keras.layers.Flatten(input_shape=([3]), # input laag.
        tf.keras.Input(shape=(16,)), # input laag.
        tf.keras.layers.Dense(48, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(24, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(12, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(2, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(1)])              # output layer

    model = fitandtest(model)
    #model.fit(lidardata,steeringdata,epochs=5)
    return model

def fittester3(lf,optimizer,nrepochs):
    #test 
    model = tf.keras.Sequential([
    #tf.keras.layers.Flatten(input_shape=([3]), # input laag.
        tf.keras.Input(shape=(16,)), # input laag.
        tf.keras.layers.Dense(24, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(48, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(72, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(36, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(1)])              # output layer
    model = fitandtest(model,optimizer,lf,nrepochs)
    #model.fit(lidardata,steeringdata,epochs=5)
    return model

def fittester4(lf,optimizer,nrepochs):
    #test 
    model = tf.keras.Sequential([
    #tf.keras.layers.Flatten(input_shape=([3]), # input laag.
        tf.keras.Input(shape=(16,)), # input laag.
        tf.keras.layers.Dense(32, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(74, activation='relu'), # 1e hidden layer
        tf.keras.layers.Dense(9, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(3, activation='relu'),  # 2e hidden layer 
        tf.keras.layers.Dense(1)])              # output layer
    model = fitandtest(model,optimizer,lf,nrepochs)
    #model.fit(lidardata,steeringdata,epochs=5)
    return model


def fitandtest(model,optimizer,lf,nrepochs):
    #print(optimizer)
    #print(lf)
    model.compile(optimizer=optimizer, 
            loss=lf,
            metrics=['mae'])

    #x=(lidardata-lidardata.min())/(lidardata.max()-lidardata.min())
    history=model.fit(lidardata,steeringdata,epochs=nrepochs,verbose=1)
    #print(history.history['accuracy'][0:3],history.history['accuracy'][-3:] )
    print(history.history['mae'][0:3],history.history['mae'][-3:] )
    results=model.evaluate(lidardata_val,steeringdata_val)
    print('loss: ' + str(results[0]),'accuracy: ' + str(results[1]) )
    sw_prediction= model.predict(lidardata_val)
    print([sw_prediction.min(),sw_prediction.mean(),sw_prediction.max()])
    
    print('_____________________________\n')
    #model.fit(lidardata,steeringdata,epochs=5)
    return model


#! ___________________________________________________________________________


if False:
    #tensorflow-model opzet.
    #test van verschillende lossfuncties.
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
    """
    test van verschillende optimizers.
    sgd komt overeen met de gradient descent. 
    
    Frank adviseert adam. 
    Deze is houdt (meer) rekening met de veranderingen uit een vorige iteratie  
    Lokale minima worden eerder vermeden. 
    """


    optimizers = [ 'adam','rmsprop','sgd']
    #optimizers = [ 'sgd']
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        print(optmzr)
        fittester(lf,optmzr,nrepochs)
        #De code hieronder snap ik nog niet echt. 

if False:
    optimizers = [ 'adam',]
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        model = fittester(lf,optmzr,nrepochs)
    model.save('C:/temp/test_tf')

    if True:
        """ 
        laden van een model en kijken of het het goede resultaat oplevert. 

        """
        model = tf.keras.models.load_model('C:/temp/tf_test')
        steering_prediction = model.predict(np.array(lidardata_val))
        figure = pp.figure()
        pp.plot(steeringdata_val)
        pp.plot(steering_prediction,'r')
        pp.show()
if False:
    optimizers = [ 'adam',]
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        model = fittester(lf,optmzr,nrepochs)
    model.save('C:/temp/test_tf')

    if True:
        """ 
        laden van een model en kijken of het het goede resultaat oplevert. 

        """
        model = tf.keras.models.load_model('C:/temp/tf_test')
        steering_prediction = model.predict(np.array(lidardata_val))
        figure = pp.figure()
        pp.plot(steeringdata_val)
        pp.plot(steering_prediction,'r')
        pp.show()


if False:
    optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.003)]
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        model = fittester(lf,optmzr,nrepochs)
    model.save('C:/temp/test_tf_v1')

    steering_prediction = model.predict(np.array(lidardata_val))
    figure = pp.figure()
    pp.plot(steeringdata_val)
    pp.plot(steering_prediction,'r')
    pp.show()


    if False:
        """ 
        laden van een model en kijken of het het goede resultaat oplevert. 

        """
        model = tf.keras.models.load_model('C:/temp/tf_test')
        steering_prediction = model.predict(np.array(lidardata_val))
        figure = pp.figure()
        pp.plot(steeringdata_val)
        pp.plot(steering_prediction,'r')
        pp.show()

if False:
    optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.003)]
    lf = tf.keras.losses.squared_hinge

    for optmzr in optimizers:
        model = fittester(lf,optmzr,nrepochs)
    model.save('C:/temp/test_tf_v2')

    steering_prediction = model.predict(np.array(lidardata_val))
    figure = pp.figure()
    pp.plot(steeringdata_val)
    pp.plot(steering_prediction,'r')
    pp.show()

if False:
    optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.003)]
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        model = fittester0(lf,optmzr,nrepochs)
    model.save('C:/temp/test_tf0_v1')

    steering_prediction = model.predict(np.array(lidardata_val))
    figure = pp.figure()
    pp.plot(steeringdata_val)
    pp.plot(steering_prediction,'r')
    pp.show()

if False:
    nrepochs = 50
    #optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.003)]
    optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.001)]
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        model = fittester3(lf,optmzr,nrepochs)
    model.save('C:/temp/lidar_tf2_v1')

    #steering_prediction = model.predict(np.array(lidardata_val))
    steering_prediction = model.predict(np.array(lidardata))
    figure = pp.figure()
    pp.plot(steeringdata)
    #pp.plot(steeringdata_val)
    pp.plot(steering_prediction,'r')
    pp.show()

if True:
    nrepochs = 200
    #optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.003)]
    optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.001)]
    lf = tf.keras.losses.mean_squared_error

    for optmzr in optimizers:
        model = fittester4(lf,optmzr,nrepochs)
    model.save('C:/temp/lidar_tf2_v2')

    #steering_prediction = model.predict(np.array(lidardata_val))
    steering_prediction = model.predict(np.array(lidardata))
    figure = pp.figure()
    pp.plot(steeringdata)
    #pp.plot(steeringdata_val)
    pp.plot(steering_prediction,'r')
    pp.show()
