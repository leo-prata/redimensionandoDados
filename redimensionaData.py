from moabb.datasets import SSVEPExo
import numpy as np
import mne

dataset = SSVEPExo()
Xraw = dataset.get_data(subjects=[1])[1]['0']['0']

events = []
corte = Xraw.get_data()[8]
print(len(corte)) 
for i in range(len(corte)):
  if corte[i] != 0:
    events.append([i,0,corte[i]]) 

events = np.array(events).astype(int)
X = mne.Epochs(Xraw, events, tmin=0, tmax=2, baseline=None).get_data()[:,:-1,:-1]
Y = events[:,2]

print(X.shape) 
print(Y.shape)
