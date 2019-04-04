import math
from matplotlib import pyplot as plt


#Parametros
alpha=0.5
beta=-(1.0/8.0)
N=31
h=[]
y=[] #respuesta al escalon
if( -((alpha/2.0)**2) > beta):
    wo= math.sqrt( -(beta+ (alpha/2.0)**2 ) )
    w= math.atan( wo/(alpha/2.0) )
    h=[]
    h.append(0)
    for i in range(1,N+1):
        h.append( (1/(2.0*wo))* ( (-beta)**((i-1)/2.0) )* math.sin( (i-1)*w) )
    y.append(0)
    for i in range(1,N):
        y.append( (1.0/(1-alpha-beta))*( 0.5 - ( beta )*h[i] - h[i+1] ) )
    plt.stem(y)
    plt.xlabel("n")
    plt.ylabel("Resp al escalon")
    plt.grid(True)
    plt.show()