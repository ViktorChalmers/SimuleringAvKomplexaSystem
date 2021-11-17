from functions import initRandomPositions, plotPeriodic, getVelocity, getGlobalAlignment,\
    globalClusteringCoefficient,getParticleInRadius,periodicBoundary,plotVoronoi
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange
from scipy.spatial import Voronoi, voronoi_plot_2d,ConvexHull
import time as time

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

def P8(L,N,v,dt,noice,steps,r,h):
    t = time.strftime("%X")
    #[position, theta] = initRandomPositions(N, L)
    #np.save('position1000', position)
    #np.save('theta1000', theta)

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
    flockIndex = getFlockIndex(position, L, r)
    fi = np.zeros([steps])
    cn = np.zeros([steps])
    thetaList = [theta]
    flockIndexList = [flockIndex]
    for i in trange(steps):

        if i == 0 or i == 10 or i == 100 or i == 1000:
            #fig, ax = plt.subplots()
            #plotPeriodic(position, L)
            plotVoronoi(position, L)
            plt.title(f"configurations after iterations = {i},r={r},noice={noice},N={N},h={h}")
            plt.savefig(f"{t},config;iter={i};r={r};noice={noice};N={N},h={h}".replace(".", ",").replace(":", ";"))
        if i>h and h>0:
            fi[i] = getGlobalAlignment(velocity, v)
            cn[i] = globalClusteringCoefficient(position, L, r)
            #print(len(flockIndexList))
            flockIndex = getFlockIndex(position, L, r)
            theta = updateTheta(thetaList[-h], flockIndexList[-h], noice, dt)
            velocity = getVelocity(thetaList[-h], v)
            position = updatePosition(position, velocity, dt, L)
            thetaList.append(theta)
            flockIndexList.append(flockIndex)
        else:
            fi[i] = getGlobalAlignment(velocity, v)
            cn[i] = globalClusteringCoefficient(position, L, r)
            flockIndex = getFlockIndex(position, L, r)
            theta = updateTheta(theta,flockIndex,noice,dt)
            velocity = getVelocity(theta, v)
            position = updatePosition(position, velocity, dt, L)
            thetaList.append(theta)
            flockIndexList.append(flockIndex)

    #fig, ax = plt.subplots()
    plotVoronoi(position, L)
    plt.title(f"configurations after iterations = {steps},r={r},noice={noice},N={N},h={h}")

    plt.savefig(f"{t},config;iter={i};r={r};noice={noice};N={N},h={h}".replace(".", ",").replace(":", ";"))
    plt.subplot()
    fig, ax = plt.subplots()
    #ax.plot(cn)
    ax.plot(fi)
    ax.plot(cn)
    plt.xlabel('timesteps t')
    plt.ylabel('fi,cn')
    plt.legend([r'$\psi$',r'$c$'])
    plt.title(f"fc iter = {steps},r={r},noice={noice},N={N},h={h}")
    plt.savefig(f"{t},fc;iter={steps};r={r};noice={noice};N={N},h={h}".replace(".", ",").replace(":", ";"))
    print(f"{t},fc;iter={steps};r={r};noice={noice};N={N}".replace(".", ",").replace(":", ";"))
    #plt.show()

