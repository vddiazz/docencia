import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
rc('text', usetex=True)

mpl.use("QtAgg")

#####

def alpha_m(l):
    return np.sqrt(-l)*np.tanh(np.sqrt(-l))

def alpha_p(l):
    return -l*np.tan(l)

##### alpha_m
"""
L = np.linspace(-5,0,500)

plt.plot(L,alpha_m(L),"r-")

plt.title(r"$\alpha(\lambda) = \sqrt{-\lambda} \tanh( \sqrt{-\lambda} )$")
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$\alpha(\lambda)$")

plt.xlim([-5,0])
plt.ylim([0,2.5])

plt.show()
"""
##### alpha_p

L1 = np.linspace(0,np.pi/2,100)
L2 = np.linspace(np.pi/2+0.01,3*np.pi/2,100)
L3 = np.linspace(3*np.pi/2+0.01,5*np.pi/2,100)

plt.plot(L1,alpha_p(L1),"r-")
plt.plot(L2,alpha_p(L2),"r-")
plt.plot(L3,alpha_p(L3),"r-")

plt.vlines(np.pi/2, -15,15, colors="k", linestyles="dashed")
plt.vlines(3*np.pi/2, -15,15, colors="k", linestyles="dashed")
plt.vlines(5*np.pi/2, -15,15, colors="k", linestyles="dashed")

plt.title(r"$\alpha(\lambda) = -\sqrt{\lambda} \tan( \sqrt{\lambda} )$")
plt.xlabel(r"$\sqrt{\lambda}$")
plt.ylabel(r"$\alpha(\lambda)$")

plt.xlim([0,8])
plt.ylim([-15,15])

plt.show()
