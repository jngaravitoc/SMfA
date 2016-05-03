import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import sys
<<<<<<< HEAD


=======
import pandas as pd
>>>>>>> 7f4f67feb5bf8d1f8238b6b5d14fb1087552abca
font = {'size':15, 'family':'serif'}
matplotlib.rc('font', **font)


# Reading data
data_name = sys.argv[1]
<<<<<<< HEAD
data = np.genfromtxt(data_name)

xi2 = data[:,3]

"""
mask = np.where((data[:,0]<85) & (data[:,0]>55) & (data[:,3]<30))[0]
data_sorted = data[mask]
print data_sorted
"""
# Length of the 2x2 matrix
=======
df = pd.read_csv(data_name, sep=' ')
data = df.as_matrix()

#i2 = data[:,3]
#ask = np.where((data[:,0]<85) & (data[:,0]>55) & (data[:,3]<30))[0]
#data_sorted = data[mask]


>>>>>>> 7f4f67feb5bf8d1f8238b6b5d14fb1087552abca
N = math.ceil(len(data)**(1./3.))

print 'The length of the matrix is going to be', N

<<<<<<< HEAD
#Finding the minimum of the xi2 
min_xi2 = np.where(data[:,3] == np.nanmin(data[:,3]))[0]


# Best parameters values:
best_o_m = data[min_xi2, 1]
best_o_l = data[min_xi2, 2]
best_H = data[min_xi2,0]
=======
#finding the minimum of the xi2
min_xi2 = np.where(data[:,3] == np.nanmin(data[:,3]))[0]
print 'index', min_xi2

# Finding the best Hubble constant value
best_H_matrix = np.where(data[:,0] == data[min_xi2[0],0])[0]

#Printing the best parameter values
>>>>>>> 7f4f67feb5bf8d1f8238b6b5d14fb1087552abca
print "omega_m: ", data[min_xi2, 1][0]
print "omega_L: ", data[min_xi2, 2][0]
print "H0: ", data[min_xi2, 0][0]
print "Max(L):", data[min_xi2,3][0]

<<<<<<< HEAD
#Making a Matrix with the best values of H_0

best_H_matrix = np.where(data[:,0] == 70)[0]

# Valuesof Omega_m and Omega_L to make the grid in the contour plot
omega_m = np.linspace(min(data[best_H_matrix,1]), max(data[best_H_matrix,1]),N)
omega_L = np.linspace(min(data[best_H_matrix,2]), max(data[best_H_matrix,2]),N)

# Making a 2x2 matrix for xi2 for the best value of H_0
# Selecting the values of xi2 from the best values of H_0
xis = data[best_H_matrix,3]
xi2_matrix = np.reshape(np.exp(-xis/2.),(int(N),int(N)))/np.nanmax(np.exp(-xis/2.))
=======
#omega_m = np.linspace(min(data[best_H_matrix,1]), max(data[best_H_matrix,1]),N)
#omega_L = np.linspace(min(data[best_H_matrix,2]), max(data[best_H_matrix,2]),N)

#print omega_m
#print min_xi2, best_H_matrix
# Making a 2x2 matrix to xi2 for the best H
#xis = data[best_H_matrix,3]
#xi2_matrix = np.reshape(np.exp(-xis/2.),(int(N),int(N)))/np.max(np.max(-xis/2.))
>>>>>>> 7f4f67feb5bf8d1f8238b6b5d14fb1087552abca

print np.nanmin(xi2_matrix)

#print xi2_matrix
<<<<<<< HEAD
levels = [1.-0.997,1.-0.94, 1.-0.681]
plt.contour(omega_m, omega_L, xi2_matrix.T)# levels=levels)
#plt.scatter(best_o_m, best_o_l)
plt.colorbar()
plt.xlabel('$\Omega_m$', fontsize=25)
plt.ylabel('$\Omega_\Lambda$', fontsize=25)
plt.show()
=======
#levels = [1-.999, 1-0.997, 1-.954, 1-.682]
#plt.contour(omega_m, omega_L, xi2_matrix, levels=levels)
#plt.colorbar()
#plt.xlabel('$\Omega_m$', fontsize=25)
#plt.ylabel('$\Omega_\Lambda$', fontsize=25)
#plt.show()
>>>>>>> 7f4f67feb5bf8d1f8238b6b5d14fb1087552abca
#plt.savefig('test_contour.png', bbox_inches='tight', dpi=300)
