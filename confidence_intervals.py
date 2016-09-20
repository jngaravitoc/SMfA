import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random

def g(xi):
    return np.exp(-xi**2./2.)

def f(M, N):
    deltax = 2.*N/(M-1.)
    sum = 0.
    def x(i):
        return -N + (2.*(i-1.)/(M-1.)*N)
    for i in range(2,M-1):
        xi = x(i)
        sum += g(xi)
    return deltax/np.sqrt(2*np.pi)*(0.5*g(x(1.)) + sum + 0.5*g(x(M)))

M = 2**12 
#print f(M, 1)
#print f(M, 2)
#print f(M, 3)
#print f(M, 4)
#print f(M, 5), f(2**13, 5), f(2**14, 5), f(2**8, 5), f(2**6, 5)

es = range(3,15)
plt.figure()
for e in es:
    plt.plot(2**e, 1. -f(2**e,5), 'o')
plt.ylim(-1e-4, 0.0012)
plt.xlabel('M')
plt.ylabel('1-f(M)')
plt.savefig('convergence_5sigma.pdf')

#######################################################################
sigma = 0.1
mean = 0.
N = int(1e7)
x1 = random.uniform(size=N)
x2 = random.uniform(size=N)
y2 = np.sqrt(-2.*np.log(x1))*np.sin(2*np.pi*x2)
y1 = np.sqrt(-2.*np.log(x2))*np.cos(2*np.pi*x1)
z1 = mean + sigma*y1 

M = 2**10
k = 2**7
ymin = -10.*sigma
ymax = 10.*sigma
deltay = (ymax - ymin)/(M-1.)

def y(i, M ):
    return ymin + ((i-1.)/(M-1.)*(ymax-ymin))

yis = [y(ii, M) for ii in range(M)]
Py, bins = np.histogram(z1, bins=yis+[y(M,M)], normed=True)
Pmax = np.max(Py)
print Pmax
Pj = [(j-1.)/(k-1.)*Pmax for j in range(k)]

def Cj(pj):
    #for py in Py:
    Cjj = 0
    for i in range(2,M-1):
        if Py[i] > pj:
            Cjj += deltay*Py[i]
        else: 
            Cjj += 0.
    return Cjj

Cjs = [Cj(pj) for pj in Pj]
plt.figure()
plt.subplot(211)
plt.plot(Pj, Cjs)
plt.xlim(0,Pmax)
plt.xlabel(r'P$_j$', fontsize=18)
plt.ylabel(r'C$_j$', fontsize=18)
C0 = 0.683
Cjs = np.array(Cjs)
lo = Cjs[Cjs < C0][0]
hi = Cjs[Cjs > C0][-1]
print lo,hi

j = np.where(lo == Cjs)[0][0]
print Cjs[j]
j1 = np.where(hi == Cjs)[0][0]
print Cjs[j1]

P0 = ((Pj[j1] - Pj[j])/(Cjs[j1] - Cjs[j])*(C0-Cjs[j])) + Pj[j]


goodis = []
for i in range(len(Py)-1):
    if Py[i] <= P0 and Py[i+1] >=P0:
        goodis.append(i)
    if Py[i] >= P0 and Py[i+1] <=P0:
        goodis.append(i)
print goodis
print P0, [Py[i] for i in goodis], [Py[i+1] for i in goodis]
assert(len(goodis) == 2)
i = goodis[0]
i1 = goodis[1]

y1 = ((yis[i+1] - yis[i])/(Py[i+1] - Py[i])*(P0-Py[i])) + yis[i]
y2 = ((yis[i1+1] - yis[i1])/(Py[i1+1] - Py[i1])*(P0-Py[i1])) + yis[i1]

print 'confidence level:', C0
print 'P0:',P0
print 'y0s:', y1, y2


plt.subplot(212)
plt.plot(bins[:-1], Py)
plt.ylabel(r'P(y)', fontsize=18)
plt.axhline(y=P0, color='k')
plt.axvline(x=y1, color='k', ls='--')
plt.axvline(x=y2, color='k', ls='--')
plt.tight_layout()
plt.savefig('Pj_Cj.pdf')
