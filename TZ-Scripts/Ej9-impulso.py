
import math
from matplotlib import pyplot as plt


#Parametros
alpha=5.0/4.0
beta=-25.0/32.0
N=31
h=[]
if( -((alpha/2.0)**2) > beta):
    wo= math.sqrt( -(beta+ (alpha/2.0)**2 ) )
    w= math.atan( wo/(alpha/2.0) )
    h=[]
    h.append(0)
    for i in range(1,N):
        h.append( (1/(2.0*wo))* ( (-beta)**((i-1)/2.0) )* math.sin( (i-1)*w) )
    plt.stem(h)
    plt.xlabel("n")
    plt.ylabel("h(n)")
    plt.grid(True)
    plt.show()