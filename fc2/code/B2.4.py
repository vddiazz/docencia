import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
rc('text', usetex=True)

mpl.use("QtAgg")

### functions

def dot_gp(t,gm,dE,w,w0):
    """
    t:      tempo
    gm:     gamma_-
    dE:     momento dipolar * campo externo
    w:      frecuencia
    w0:     frecuencia de resonancia
    """
    hbar = 1.055e-34 # (J·s)

    return ((dE)/(2*1j*hbar))*(np.exp(1j*(w-w0)*t) + np.exp(-1j*(w+w0)*t))*gm

def dot_gm(t,gp,dE,w,w0):
    """
    t:      tempo
    gp:     gamma_+
    dE:     momento dipolar * campo externo
    w:      frecuencia
    w0:     frecuencia de resonancia
    """   
    hbar = 1.055E-34 # (J·s)
    
    return ((dE)/(2*1j*hbar))*(np.exp(1j*(w+w0)*t) + np.exp(-1j*(w-w0)*t))*gp

def RK4_full(dot_gm,dot_gp,const,incs,time,out):
    """
    dot_gm: 
    dot_gp:
    const: 
    incs:
    time:
    out:
    """

    # Constantes
    dE, w, w0 = const

    # Condicións iniciais
    t0       = 0.0
    tf, dt   = time
    N        = int(tf/dt)
    gm, gp   = incs

    # Listas para os resultados    
    Lgm = []; Lgp = []

    # Bucle principal (Runge-Kutta de 4º orde)
    t = t0

    for n in range(1,N+1,1):
        
        # Gardar paso anterior
        Lgm.append(gm)
        Lgp.append(gp)

        # Calcular seguinte paso
        t = t+dt

        k1_gm   = dt*dot_gm(t,gp,dE,w,w0)
        k1_gp   = dt*dot_gp(t,gm,dE,w,w0)

        k2_gm   = dt*dot_gm(t,gp + k1_gp/2.,dE,w,w0)
        k2_gp   = dt*dot_gp(t,gm + k1_gm/2.,dE,w,w0)

        k3_gm   = dt*dot_gm(t,gp + k2_gp/2.,dE,w,w0)
        k3_gp   = dt*dot_gp(t,gm + k2_gm/2.,dE,w,w0)

        k4_gm   = dt*dot_gm(t,gp + k3_gp/2.,dE,w,w0)
        k4_gp   = dt*dot_gp(t,gm + k3_gm/2.,dE,w,w0)

        # Actualizar variables
        gm      = gm + k1_gm/6. + k2_gm/3. + k3_gm/3. + k4_gm/6.
        gp      = gp + k1_gp/6. + k2_gp/3. + k3_gp/3. + k4_gp/6.

    # Gardar resultados
    np.save(f"{out}/gm.npy", Lgm)
    np.save(f"{out}/gp.npy", Lgp)

    return Lgm, Lgp

### 

dE    = 1E-30 # (J) 
#w     = 2*np.pi*1E-6 # (s)
w0    = 2*np.pi*4.17E-11 # (s) para o NH3
w = w0

t0    = 0.
tf    = 1E-3
dt    = 1E-10

gm0   = 1.#1/np.sqrt(2)  # => c_-
gp0   = 0.#-1/np.sqrt(2) # => c_+

const = [dE,w,w0]
incs  = [gm0,gp0]
time  = [tf,dt]
out   = "/home/vddiazz/Desktop"

Lgm, Lgp = RK4_full(dot_gm,dot_gp,const,incs,time,out)

### plots

T = np.arange(t0,tf,dt)

plt.plot(T,Lgm,'r-',label=r'$\gamma_- (t)$')
plt.plot(T,Lgp,'b-',label=r'$\gamma_+ (t)$')

plt.xlim([0,tf])
plt.ylim([-1,1])

plt.legend()
plt.show()
