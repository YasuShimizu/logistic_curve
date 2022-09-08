import numpy as np
import matplotlib.pyplot as plt


t_inf=100
k=13.81/t_inf
sigma0=0.001
tau=np.linspace(0,1,50)
sigma=sigma0/(sigma0+(1-sigma0)*np.exp(-k*t_inf*tau))

fig,ax=plt.subplots(figsize = (12,9))
tmin=0; tmax=1; smin=0; smax=1
im=ax.set_xlim(tmin,tmax)
im=ax.set_ylim(smin,smax)
im=ax.set_title("Logistic Curve",size='30')
im=ax.set_xlabel("$\\tau$",size='25')
im=ax.set_ylabel("$\sigma$",size='25')
for tick in ax.get_xticklabels():
    tick.set(fontsize=25)
for tick in ax.get_yticklabels():
    tick.set(fontsize=25)


im=ax.plot(tau,sigma)
im=plt.savefig('logistic.png')
plt.clf()
plt.close()
#plt.show()

