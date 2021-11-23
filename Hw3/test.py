from P1 import P1
import matplotlib.pyplot as plt
import numpy as np


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


beta = [0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
R = np.zeros(len(beta))
gammalist = [0.01,0.02]
for j in range(len(gammalist)):
    gamma = gammalist[j]
    for i in range(len(beta)):
        probDiffusion = beta[i]
        R[i] = P1(lattice=100,   nSuspectible=990, nInfected=10, nRecovered=0, nDead=0,  probRandomWalk=0.8, probDiffusion = probDiffusion,      probRecover=gamma,   probDeath = 0,  probSusceptible = 0,plott=False)
    
    plt.legend(f"gamma = {gamma}")
    print(f"----------------------------------{R},{beta}")
    plt.plot(beta,R,"o")
plt.title("Final number of recovered agends as a function of the infection rate")
plt.legend(gammalist)
plt.savefig(f"AverageR_over_multiple_Beta".replace(".",","))