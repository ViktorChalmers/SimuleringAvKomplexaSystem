from P1 import P1
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm,trange


#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=0.6,    probRecover=0.005,)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=0.7,    probRecover=0.005,)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=0.8,    probRecover=0.005,)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=0.9,    probRecover=0.005,)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.005,)

#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=0.6,    probRecover=0.01,)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=0.7,    probRecover=0.01,)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=0.8,    probRecover=0.01,)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=0.9,    probRecover=0.01,)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.01,)

#P1(lattice = 100,nSuspectible = 990,nInfected = 10,nRecovered = 0,nDead = 0,probRandomWalk=0.8,probDiffusion = 0.6,probRecover = 0.001,)

#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.01,   probDeath = 0.001,  probSusceptible = 0)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.01,   probDeath = 0.005,  probSusceptible = 0)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.01,   probDeath = 0.01,  probSusceptible = 0)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.01,   probDeath = 0.05,  probSusceptible = 0)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.01,   probDeath = 0.1,  probSusceptible = 0)
#P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.01,   probDeath = 0.01,  probSusceptible = 0)



