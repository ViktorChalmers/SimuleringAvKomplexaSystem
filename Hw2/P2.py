from functions import initRandomPositions, getGlobalAlignment,plotPeriodic,getParticleInRadius
import matplotlib.pyplot as plt
import numpy as np

def P2(N,L,nr,r):
    [position, theta] = initRandomPositions(N,L)
    globalAlignment = getGlobalAlignment(position,nr,r,L)

    posIndex = getParticleInRadius(position, nr, L, r)
    ret = np.zeros([len(posIndex), 2])
    for i in range(len(posIndex)):
        ret[i] = position[posIndex[i]]

    plt.title(f"Global alignment = {globalAlignment}")
    [fig,ax]=plotPeriodic(position,L,nr,r=r)
    plt.plot(ret[:, 0], ret[:, 1], "*", color="r")
    plt.show()

    return globalAlignment
