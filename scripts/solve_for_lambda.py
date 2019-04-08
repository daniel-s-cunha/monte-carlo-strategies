import numpy as np
import math
from matplotlib import pyplot as plt

c = 0
Phi_c = 0.5

def rejection_func(lambda0):
	return ((math.sqrt(2*math.pi))*lambda0*(1-Phi_c)/math.exp((lambda0**2 - 2*lambda0*c)/2))


lambda0 = np.arange(0,2,0.01)

rf_axis = []
for i in lambda0:
	rf_axis.append(rejection_func(i))


plt.scatter(lambda0,rf_axis)
plt.show()


















