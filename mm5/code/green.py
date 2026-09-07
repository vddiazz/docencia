import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
rc('text', usetex=True)

mpl.use("QtAgg")

#####

def G(prob: str,x,z):
    
    if prob == "4.10.a":
        return np.where(
            x > z,
            -z*(1-x),
            (-1+z)*x
        )
    
    elif prob == "4.10.d":
         return np.where(
            x > z,
            z/2*(x-2),
            (z-2)/2*x
        )

    elif prob == "4.12":
         return np.where(
            x > z,
            np.sin(x-z),
            0
        )

    elif prob == "4.13":
         return np.where(
            x > z,
            -1./(2*z) * (1-x**2),
            -1./(2*z**3) * (1-z**2)*x**2
        )

    elif prob == "4.15":
        l = 12
        return np.where(
            x > z,
            -(z**(l+2)/(2*l+1))*x**(-l-1),
            -(z**(-l+1)/(2*l+1))*x**l
        )

###

x0 = 0.; xf = 50.
z0 = 0.; zf = 50.

Xp = np.linspace(x0+0.001,xf,1000)
Zp = np.linspace(z0+0.001,zf,1000)
X,Z = np.meshgrid(Xp,Zp)

G_vals = G("4.15",X,Z)

###

plt.figure(figsize=(7,6))

# x axis
xoriginal = np.linspace(0, len(G_vals[:,0]), len(G_vals[:,0])+1)
xrescaled = np.linspace(x0, xf, len(G_vals[:,0])+1)
xticks = [0, xf*1/5., xf*2/5., xf*3/5., xf*4/5., xf]
xtick_pos = [np.argmin(np.abs(xrescaled - val)) for val in xticks]

# y axis
yoriginal = np.linspace(0, len(G_vals[0,:]), len(G_vals[0,:])+1)
yrescaled = np.linspace(z0, zf, len(G_vals[0,:])+1)
yticks = [0, zf*1/5., zf*2/5., zf*3/5., zf*4/5., zf]
ytick_pos = [np.argmin(np.abs(yrescaled - val)) for val in yticks]

plt.minorticks_on()

plt.xticks(xtick_pos, xticks)
plt.yticks(ytick_pos, yticks)

plt.xlim([0,1000])
plt.ylim([0,1000])

plt.xlabel(r"$x$")
plt.ylabel(r"$z$")
plt.title(r"$G(x,z)$")

im = plt.imshow(G_vals, aspect='auto', origin='lower', cmap="Spectral")

cbar = plt.colorbar(im)
cbar.set_ticks(np.linspace(G_vals.min(),G_vals.max(),5))

plt.show() 
