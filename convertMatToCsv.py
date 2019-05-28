import scipy.io
import numpy as np


data = scipy.io.loadmat("name_ordre.mat")

for i in data:
    if '__' not in i and 'readme' not in i:
        np.savetxt(("name_ordre.csv"), data[i], fmt='%s',delimiter=',')