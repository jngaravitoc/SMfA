import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import sys
import pandas as pd
font = {'size':15, 'family':'serif'}
matplotlib.rc('font', **font)


# Reading data
data_name = sys.argv[1]
df = pd.read_csv(data_name, sep=' ')
data = df.as_matrix()

#i2 = data[:,3]
#ask = np.where((data[:,0]<85) & (data[:,0]>55) & (data[:,3]<30))[0]
#data_sorted = data[mask]


N = math.ceil(len(data)**(1./3.))

print 'The length of the matrix is going to be', N

#finding the minimum of the xi2
min_xi2 = np.where(data[:,3] == np.nanmin(data[:,3]))[0]
print 'index', min_xi2

# Finding the best Hubble constant value
best_H_matrix = np.where(data[:,0] == data[min_xi2[0],0])[0]

#Printing the best parameter values
print "omega_m: ", data[min_xi2, 1][0]
print "omega_L: ", data[min_xi2, 2][0]
print "H0: ", data[min_xi2, 0][0]
print "Max(L):", data[min_xi2,3][0]

#omega_m = np.linspace(min(data[best_H_matrix,1]), max(data[best_H_matrix,1]),N)
#omega_L = np.linspace(min(data[best_H_matrix,2]), max(data[best_H_matrix,2]),N)

#print omega_m
#print min_xi2, best_H_matrix
# Making a 2x2 matrix to xi2 for the best H
#xis = data[best_H_matrix,3]
#xi2_matrix = np.reshape(np.exp(-xis/2.),(int(N),int(N)))/np.max(np.max(-xis/2.))


#print xi2_matrix
#levels = [1-.999, 1-0.997, 1-.954, 1-.682]
#plt.contour(omega_m, omega_L, xi2_matrix, levels=levels)
#plt.colorbar()
#plt.xlabel('$\Omega_m$', fontsize=25)
#plt.ylabel('$\Omega_\Lambda$', fontsize=25)
#plt.show()
#plt.savefig('test_contour.png', bbox_inches='tight', dpi=300)
