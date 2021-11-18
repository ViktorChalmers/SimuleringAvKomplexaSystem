from functions import initRandomPositions, plotPeriodic, getVelocity, getGlobalAlignment,\
    globalClusteringCoefficient,getParticleInRadius,periodicBoundary,plotVoronoi
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange
from scipy.spatial import Voronoi, voronoi_plot_2d,ConvexHull

def updateTheta(theta,flockIndex,noice,dt):


    mean = np.zeros(len(theta))
    for j in range(len(theta)):
        wn = np.random.rand(1) * noice - noice / 2
        meansin=0
        meancos=0

        for i in range(len(flockIndex[j])):
            meansin = meansin + np.sin(theta[flockIndex[j][i]])
            meancos = meancos + np.cos(theta[flockIndex[j][i]])
        mean[j] = np.arctan(meansin/meancos)
        theta[j] = np.arctan(meansin/meancos)+wn

    return theta

def updatePosition(position,velocity,dt,L):
    position = position+velocity*dt
    return periodicBoundary(position, L)

def getFlockIndex(position, L, r):
    flockIndex = []
    for i in range(len(position)):
        flockIndex.append(getParticleInRadius(position, i, L, r))
    return flockIndex

def P4(L,N,v,dt,noice,steps,r):


    #[position, theta] = initRandomPositions(100,1000)
    #np.save('position100L1000', position)
    #np.save('theta100L1000', theta)

    if N == 100 and L == 100:
        position = np.load('position.npy')
        theta = np.load('theta.npy')
    elif N == 1000 and L == 100:
        position = np.load('position1000L100.npy')
        theta = np.load('theta1000L100.npy')
    elif N == 100 and L == 1000:
        position = np.load('position100L1000.npy')
        theta = np.load('theta100L1000.npy')




    #print(open("E:\python.txt").read())

    velocity = getVelocity(theta, v)
    #plotPeriodic(position, L)
    fi = getGlobalAlignment(velocity, v)
    cn = globalClusteringCoefficient(position, L, r)

    fi = np.zeros([steps])
    cn = np.zeros([steps])
    for i in trange(steps):
        if i == 0 or i == 10 or i == 100 or i == 500 or i == 1000:
            #fig, ax = plt.subplots()
            #plotPeriodic(position, L)
            plotVoronoi(position, L)
            plt.title(f"configurations after iterations = {i},r={r},noice={noice},N={N}")
            plt.savefig(f"config;iter={i};r={r};noice={noice};N={N}".replace(".",","))
        fi[i] = getGlobalAlignment(velocity, v)
        cn[i] = globalClusteringCoefficient(position, L, r)
        flockIndex = getFlockIndex(position, L, r)
        theta = updateTheta(theta,flockIndex,noice,dt)
        velocity = getVelocity(theta, v)
        position = updatePosition(position, velocity, dt, L)

    #fig, ax = plt.subplots()
    plotVoronoi(position, L)
    plt.title(f"configurations after iterations = {steps},r={r},noice={noice},N={N}")
    plt.savefig(f"config;iter={i};r={r};noice={noice};N={N}".replace(".",","))
    plt.subplot()
    fig, ax = plt.subplots()
    #ax.plot(cn)
    ax.plot(fi)
    ax.plot(cn)
    plt.xlabel('timesteps t')
    plt.ylabel('fi,cn')
    plt.legend([r'$\psi$',r'$c$'])
    plt.savefig(f"fc;iter={steps};r={r};noice={noice};N={N}".replace(".",","))

    #plt.show()

