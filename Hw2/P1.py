import numpy as np
import matplotlib.pyplot as plt
from functions import initRandomPositions,getParticleInRadius,plotPeriodic,displaceParticles


def P1(L,r,nr,N,part,step=1):
    boundaryLength = L
    flockingRadius = r
    particleNr = nr
    nParticles = N

    [position, theta] = initRandomPositions(nParticles, boundaryLength)

    if part=="a":
        posIndex = getParticleInRadius(position,particleNr,r = flockingRadius,L = boundaryLength)

        ret = np.zeros([len(posIndex), 2])
        for i in range(len(posIndex)):
            ret[i] = position[posIndex[i]]

        [fig,ax] = plotPeriodic(position, boundaryLength)
        plt.plot(ret[:, 0], ret[:, 1], "*",color="r")
        circle1 = plt.Circle((position[particleNr]), flockingRadius, fill=False)
        ax.add_patch(circle1)
        print(posIndex)
        plt.show()
    elif part=="b":
        plt.plot(position[:, 0], position[:, 1], "o")
        position = displaceParticles(position, step, L)
        plt.plot(position[:, 0], position[:, 1], "o")
        plt.xlim(-L / 2, L / 2)
        plt.ylim(-L / 2, L / 2)
        plt.show()

#plt.plot(position[:, 0], position[:, 1], "o")
#vec2 = displaceParticles(position, 1,boundaryLength)
#plt.plot(vec2[:,0],vec2[:,1],"o")
#plt.xlim(-boundaryLength / 2, boundaryLength / 2)
#plt.ylim(-boundaryLength / 2, boundaryLength / 2)


#plt.show()
