from P1 import P1
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm,trange

def P3():
    avg = 1
    beta = 0.6
    gammalist = [0.01,0.02]
    muList = [0.0001,0.0005,0.001,0.005,0.01]
    for j in range(len(gammalist)):
        R = np.zeros(len(muList))
        gamma = gammalist[j]
        for i in range(len(muList)):
            pDeath = muList[i]
            for k in range(avg):
                R[i] +=  P1(lattice=100,
                                nSuspectible=990,
                                nInfected=10,
                                nRecovered=0,
                                nDead=0,
                                probRandomWalk=0.8,
                                probDiffusion = beta,
                                probRecover=gamma,
                                probDeath = pDeath,
                                probSusceptible = 0,
                                plott=2
                                )/avg
            print(f"----------------------------------gamma={gammalist[j]}, R={R[i]}, beta={muList[i]}")
        plt.plot(muList,R,"o")
        np.save(f"D(beta,death={pDeath})".replace(".",","), R)


    plt.title("Final number of dead agends as a function of the mortality rate")
    plt.legend(gammalist)

    plt.savefig(f"muDependency".replace(".",","))
    plt.show()