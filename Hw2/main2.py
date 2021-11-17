import numpy as np
import matplotlib.pyplot as plt
from P1 import P1
from P2 import P2
from P3 import P3
from P4 import P4
from P8 import P8

#P1(L=5,r=2,nr=0,N=10,part = "a",step=1)
#P2(N=15,L=5,r=2,nr=0)
#P3()
#P4(L=100,N=100,v=1,dt=1,noice=0.01,steps=20,r=1)
#P4(L=100,N=100,v=1,dt=1,noice=0.01,steps=10**4,r=2)
#P4(L=100,N=100,v=1,dt=1,noice=0.01,steps=10**4,r=10)

#P4(L=100,N=100,v=1,dt=1,noice=0.1,steps=10**4,r=1)
#P4(L=100,N=100,v=1,dt=1,noice=0.1,steps=10**4,r=2)
#P4(L=100,N=100,v=1,dt=1,noice=0.1,steps=10**4,r=10)

#P4(L=100,N=1000,v=1,dt=1,noice=0.01,steps=10**4,r=1)
#P4(L=100,N=1000,v=1,dt=1,noice=0.1,steps=10**4,r=1)

P8(L=1000,N=100,v=3,dt=1,noice=0.4,steps=3000,r=20,h=2)
P8(L=1000,N=100,v=3,dt=1,noice=0.4,steps=3000,r=20,h=25)

