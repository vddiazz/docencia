import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
rc('text', usetex=True)

mpl.use("QtAgg")

#####

def auto_m(m,x):
    return np.exp(-x)*np.sin(m*np.pi*x)

#####

X = np.linspace(0,1,100)

#plt.plot(X,auto_m(0,X), label=r"$m=0$")
plt.plot(X,auto_m(1,X), label=r"$m=1$")
plt.plot(X,auto_m(2,X), label=r"$m=2$")
plt.plot(X,auto_m(3,X), label=r"$m=3$")

plt.hlines(0, 0,1, colors="k", linestyles="dashed")

plt.title(r"$y_m(x) = e^{-x} \sin(m \pi x)$")
plt.xlabel(r"$x$")
plt.ylabel(r"$y_m(x)$")

plt.xlim([0,1])

plt.legend(facecolor='white', edgecolor='black', fancybox=False)
plt.show()
