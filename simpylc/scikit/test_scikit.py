import os
import numpy as np
import sklearn
from matplotlib import pyplot as pp
from sklearn.neural_network import MLPRegressor

#from matplotlib import pyplot as pp

path_input = r'C:\Users\marcr\MakeAIWork\simpylc\simulations\car\control_client'
lidar_input = 'lidar.samples_v1'
lidar_array = np.genfromtxt(os.path.join(path_input,lidar_input))

#10 procent reserveren voor validatie
i = lidar_array.shape[0]//100
lidardata =    lidar_array[:-i,0:16] # Dit is de input.
steeringdata = lidar_array[:-i,16] # Dit komt overeen met het label/output
lidardata_val =    lidar_array[-i:,0:16] # Dit is de input.
steeringdata_val = lidar_array[-i:,16] # Dit komt overeen met het label/output

#interessante parameters: 
#   random_state: voor gelijk houden gewichtsfactoren voor verschillende trainingssessies. 
#   warm_start: voortborduren op een vorige fit.
#   beta_1, beta_2, epsilon: speciale factor voor  
#    

mlpregr =MLPRegressor(hidden_layer_sizes=(16,72,9), activation='relu',  solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.003, max_iter=200, shuffle=True, random_state=None, tol=0.0001, verbose=True, 
 warm_start=False, early_stopping=True, validation_fraction=0.2, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10)

p = mlpregr.fit(lidardata,steeringdata)
print(p)
steeringdata_pred = mlpregr.predict(lidardata)

if False:
    fig = pp.figure()
    pp.figure(fig)
    pp.plot(steeringdata)
    pp.plot(steeringdata_pred,'r')
