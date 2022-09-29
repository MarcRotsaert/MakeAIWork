
import tensorflow as tf
import numpy as np
import os

from matplotlib import pyplot as pp




path_input = r'C:\Users\marcr\MakeAIWork\simpylc\simulations\car\control_client'
lidar_input = 'lidar.samples_v1'
lidar_array = np.genfromtxt(os.path.join(path_input,lidar_input))

#x procent reserveren voor validatie
i = lidar_array.shape[0]//20
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
    history=model.fit(lidardata,steeringdata,use_multiprocessing=True, epochs=nrepochs,verbose=1)
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
    """
    Verschillende resultaten voor 10 epochs, zoals af te leiden uit de loss-functie

    """
    #tf.random.set_seed(111)
    epochsinstances = 10*[10]
    optmzr = 'adam' 
    lf = tf.keras.losses.mean_squared_error

    evaldata=[]
    for nrepochs in epochsinstances:
        tf.random.set_seed(111) 
        nrepochs = 10
        #optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.003)]
        optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.001)]

        #for optmzr in optimizers:
        model = fittester4(lf,optmzr,nrepochs)
        #model.save('C:/temp/experiment_tf2_v2')
        evaldata.append(model.evaluate(lidardata_val,steeringdata_val))
        #steering_prediction = model.predict(np.array(lidardata_val))
        steering_prediction = model.predict(np.array(lidardata))
        
        if False:
            figure = pp.figure()
            pp.plot(steeringdata)
            #pp.plot(steeringdata_val)
            pp.plot(steering_prediction,'r')
            pp.show()
    fig = pp.figure(figsize=[10,22])
    pp.plot(np.array(evaldata)[:,0])
    pp.title('Results Loss-function after 10 epochs')
    pp.ylabel('Loss after last epoch')
    pp.xlabel('Attempt nr.')
    pp.show()
    fig.savefig('C:/temp/experimental_epoch.png')


if False:
    """
    Verschillende resultaten voor 10 epochs, zoals af te leiden uit de loss-functie

    """
    #tf.random.set_seed(111)
    epochinstances = [10,30,80,100,200,400]
    optmzr = 'adam' 
    lf = tf.keras.losses.mean_squared_error

    optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.001)]
    evaldata=[]
    for nrepochs in epochinstances:
        valloss_min=1000
        for i in range(4):
            #tf.random.set_seed(111) 
            #for optmzr in optimizers:
            model = fittester4(lf,optmzr,nrepochs)
            #model.save('C:/temp/experiment_tf2_v2')
            evaldatatemp = model.evaluate(lidardata_val,steeringdata_val)
            if evaldatatemp[0]<valloss_min:
                valloss_min = evaldatatemp[0]
        evaldata.append(valloss_min)
        #steering_prediction = model.predict(np.array(lidardata))
        if False:
            figure = pp.figure()
            pp.plot(steeringdata)
            #pp.plot(steeringdata_val)
            pp.plot(steering_prediction,'r')
            pp.show()
    fig = pp.figure(figsize=[10,22])
    pp.figure(fig)
    pp.plot(epochinstances,np.array(evaldata))
    pp.title('Results validation Loss-function')
    pp.ylabel('Loss after last epoch')
    pp.xlabel('nr. epochs')
    pp.show()
    fig.savefig('C:/temp/experimental_epoch_2.png')

if False:
    """
    Verschillende resultaten voor 10 epochs, zoals af te leiden uit de loss-functie

    """
    #tf.random.set_seed(111)
    epochinstances = [3,6,10,15,20,30]
    optmzr = 'adam' 
    lf = tf.keras.losses.mean_squared_error

    optimizers = [ tf.keras.optimizers.Adam(learning_rate=0.001)]
    evaldata=[]
    #fig2 = pp.figure(figsize=[20,44] )
    
    for nrepochs in epochinstances:
        valloss_min=1000
        modelmin= None
        for i in range(4):
            #tf.random.set_seed(111) 
            #for optmzr in optimizers:
            model = fittester4(lf,optmzr,nrepochs)
            #model.save('C:/temp/experiment_tf2_v2')
            evaldatatemp = model.evaluate(lidardata_val,steeringdata_val)
            if evaldatatemp[0]<valloss_min:
                valloss_min = evaldatatemp[0]
                modelmin=model
        evaldata.append(valloss_min)
        #pp.figure(fig2)
        #pp.plot(steeringdata_val)
        #pp.plot(modelmin.predict(lidardata_val,steeringdata_val),'r')
        #steering_prediction = model.predict(np.array(lidardata))
        if False:
            figure = pp.figure()
            pp.plot(steeringdata)
            #pp.plot(steeringdata_val)
            pp.plot(steering_prediction,'r')
            pp.show()
    fig = pp.figure(figsize=[10,22])
    pp.figure(fig)
    pp.plot(epochinstances,np.array(evaldata))
    pp.title('Results validation Loss-function')
    pp.ylabel('Loss after last epoch')
    pp.xlabel('nr. epochs')
    pp.show()
    fig.savefig('C:/temp/experimental_epoch_3.png')


if True:
    """
    Verschillende learning rates, 
    voor 10 epochs.

    """
    #tf.random.set_seed(111)
    nrepochs = 10
    optmzr = 'adam' 

    learningrates =[0.1, 0.05,0.03,0.01,0.003,0.001]

    lf = tf.keras.losses.mean_squared_error

    #fig2 = pp.figure(figsize=[20,44] )
    evaldata=[]
    for lr in learningrates:
        valloss_min=1000
        modelmin= None
        for i in range(4):
            optmzr =  tf.keras.optimizers.Adam(learning_rate=lr)
            model = fittester4(lf,optmzr,nrepochs)
            evaldatatemp = model.evaluate(lidardata_val,steeringdata_val)
            if evaldatatemp[0]<valloss_min:
                valloss_min = evaldatatemp[0]
                modelmin=model
        evaldata.append(valloss_min)
        #pp.figure(fig2)
        #pp.plot(steeringdata_val)
        #pp.plot(modelmin.predict(lidardata_val,steeringdata_val),'r')
        #steering_prediction = model.predict(np.array(lidardata))
    fig = pp.figure(figsize=[10,22])
    pp.figure(fig)
    pp.plot(learningrates,np.array(evaldata))
    pp.title('Results validation Loss-function')
    pp.ylabel('Loss after last epoch')
    pp.xlabel('learning rate')
    pp.show()
    fig.savefig('C:/temp/experimental_epoch_4.png')
