import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import sys

font = {'size':15, 'family':'serif'}
matplotlib.rc('font', **font)


# Reading data
data_name = sys.argv[1]
data = np.loadtxt(data_name)

N = math.ceil(len(data)**(1./3.))

print 'The length of the matrix is going to be',N

#finding the minimum of the xi2
min_xi2 = np.where(data[:,3] == min(data[:,3]))[0]
# Finding the best Hubble constant value
best_H_matrix = np.where(data[:,0] == data[min_xi2[0],0])[0]


omega_m = np.linspace(min(data[best_H_matrix,1]), max(data[best_H_matrix,1]), N)
omega_L = np.linspace(min(data[best_H_matrix,2]), max(data[best_H_matrix,2])    , N)

print omega_m
print min_xi2, best_H_matrix
# Making a 2x2 matrix to xi2 for the best H
xis = data[best_H_matrix,3]
xi2_matrix = np.reshape(xis,(int(N),int(N)))


print xi2_matrix
plt.contour(omega_m, omega_L, xi2_matrix)
plt.colorbar()
plt.xlabel('$\Omega_m$', fontsize=25)
plt.ylabel('$\Omega_\Lambda$', fontsize=25)
plt.savefig('test_contour.png', bbox_inches='tight', dpi=300)

