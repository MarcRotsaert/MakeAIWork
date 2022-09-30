import os
import numpy as np
import sklearn
from matplotlib import pyplot as pp
from sklearn.neural_network import MLPRegressor

import pickle

#from matplotlib import pyplot as pp

path_input = r'C:\Users\marcr\MakeAIWork\simpylc\simulations\car\control_client'
sonar_input = 'sonar.samples_v1'
sonar_array = np.genfromtxt(os.path.join(path_input,sonar_input))

#10 procent reserveren voor validatie
i = sonar_array.shape[0]//100
sonardata =    sonar_array[:-i,0:-1] # Dit is de input.
steeringdata = sonar_array[:-i,-1] # Dit komt overeen met het label/output
sonardata_val =    sonar_array[-i:,0:-1] # Dit is de input.
steeringdata_val = sonar_array[-i:,-1] # Dit komt overeen met het label/output

#interessante parameters: 
#   random_state: voor gelijk houden gewichtsfactoren voor verschillende trainingssessies. 
#   warm_start: voortborduren op een vorige fit.
#   beta_1, beta_2, epsilon: speciale factor voor  
#    

tel=1
lossscore=100
while lossscore>25:
    mlpregr = MLPRegressor(hidden_layer_sizes=(24,74,12,4), activation='relu',  solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.001, max_iter=100, shuffle=True, random_state=None, tol=0.0001, verbose=True, 
    warm_start=False, early_stopping=True, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10)

    p = mlpregr.fit(sonardata,steeringdata)
    print(p)
    if lossscore>p.loss_:
        lossscore = p.loss_
    tel += 1
    if tel>5:
        break

if tel>5:
    print('damned')
else:
    with open(r'C:\temp\scikit_sonar_v1','wb') as g:
        pickle.dump(mlpregr,g)
    steeringdata_pred = mlpregr.predict(sonardata)
    #steeringdata_pred = mlpregr.predict_proba(sonardata)
    if True:
        fig = pp.figure()
        pp.figure(fig)
        pp.plot(steeringdata)
        pp.plot(steeringdata_pred,'r')
        pp.show()

if False:
    fig = pp.figure()
    pp.figure(fig)
    pp.plot(steeringdata)
    pp.plot(steeringdata_pred,'r')
    pp.show()
