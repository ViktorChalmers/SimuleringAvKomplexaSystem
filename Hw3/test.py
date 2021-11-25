from P1 import P1
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm,trange
from P3 import P3
from P4 import P4


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

#P3()
#P4(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=1, probDiffusion=0.5,      probRecover=0.01,   probDeath = 0,  probSusceptible = 0,stepLock = 1)
#P4(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=1, probDiffusion=0.5,      probRecover=0.01,   probDeath = 0,  probSusceptible = 0,stepLock = 100)
#P4(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=1, probDiffusion=0.5,      probRecover=0.01,   probDeath = 0,  probSusceptible = 0,stepLock = 200)
#P4(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=1, probDiffusion=0.5,      probRecover=0.01,   probDeath = 0,  probSusceptible = 0,stepLock = 300)
#P4(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=1, probDiffusion=0.5,      probRecover=0.01,   probDeath = 0,  probSusceptible = 0,stepLock = 700)
#P4(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=1, probDiffusion=0.5,      probRecover=0.01,   probDeath = 0,  probSusceptible = 0,stepLock = 1000)
#P4(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=1, probDiffusion=0.5,      probRecover=0.01,   probDeath = 0,  probSusceptible = 0,stepLock = 1200)
#P4(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=1, probDiffusion=0.5,      probRecover=0.01,   probDeath = 0,  probSusceptible = 0,stepLock = 50)

P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion=1,      probRecover=0.02,   probDeath = 0,  probSusceptible = 0.001)