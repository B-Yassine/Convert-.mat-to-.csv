import scipy.io
import numpy as np

data = scipy.io.loadmat("yourFile.mat")

for i in data:
    if '__' not in i and 'readme' not in i:
        np.savetxt(("yourFile.csv"), data[i], delimiter=',')
 
