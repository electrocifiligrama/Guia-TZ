
import cmath
import numpy as np
import math
import pylab
import matplotlib.pyplot as plt

alpha=5.0/4.0
beta=-(25.0/32.0)
H= []
fase= []
w = np.arange(0,2*math.pi,0.01)
for i in range(0,len(w)):
    z= cmath.exp(complex(0,w[i]))
    H.append( 0.5* (1.0/ ((z**2)-alpha*z-beta) ) )
    fase.append( math.degrees(cmath.phase(H[i])))

H_array = np.array(H)
mag_db =20*np.log10(np.abs(H_array))
plt.subplot(2,1,1)
plt.title("Respuesta en frecuencia")
plt.plot(w,mag_db)
plt.xlabel("w(rad/seg")
plt.ylabel("|H(w)|(dB)")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(w,fase)
plt.xlabel("w(rad/seg")
plt.ylabel("fase de H(w)")
plt.grid(True)

plt.show()

