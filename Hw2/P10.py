from functions import initRandomPositions, plotPeriodic, getVelocity, getGlobalAlignment,\
    globalClusteringCoefficient,periodicBoundary,plotVoronoi
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange
from scipy.spatial import Voronoi, voronoi_plot_2d,ConvexHull

def getParticleInRadius(x, nr, L, r,k):
    nParticles = len(x)
    norm = np.zeros([len(x), 1])
    posIndex = [nr]

    #for i in range(nParticles):
    #    norm[i] = np.linalg.norm(x[i] - x[nr])
    #normSort = np.sort(norm,axis=0)
    #print(norm)
    #print(normSort)
    #for i in range(k+1):
       # np.append(posIndex, i)
       # if normSort[i] < r and normSort[i] != 0:
       #     iii = np.where(norm == normSort[i])[0]
      #      #print(iii)
      #      posIndex.append(iii[0])

    xCopyDown = np.copy(x)
    xCopyDown[:, 1] = xCopyDown[:, 1] - L

    xCopyUp = np.copy(x)
    xCopyUp[:, 1] = xCopyUp[:, 1] + L

    xCopyRight = np.copy(x)
    xCopyRight[:, 0] = xCopyRight[:, 0] + L

    xCopyLeft = np.copy(x)
    xCopyLeft[:, 0] = xCopyLeft[:, 0] - L

    xCopyDiag1 = np.copy(x)
    xCopyDiag1[:, :] = xCopyDiag1[:, :] + L

    xCopyDiag2 = np.copy(x)
    xCopyDiag2[:, :] = xCopyDiag2[:, :] - L

    xCopyDiag3 = np.copy(x)
    xCopyDiag3[:, 0] = xCopyDiag3[:, 0] + L
    xCopyDiag3[:, 1] = xCopyDiag3[:, 1] - L

    xCopyDiag4 = np.copy(x)
    xCopyDiag4[:, 0] = xCopyDiag4[:, 0] - L
    xCopyDiag4[:, 1] = xCopyDiag4[:, 1] + L

    xCopy = [x, xCopyDown, xCopyUp, xCopyRight, xCopyLeft,
             xCopyDiag1, xCopyDiag2, xCopyDiag3, xCopyDiag4]

    norm = np.zeros([len(xCopy), nParticles])
    for i in range(len(xCopy)):
        for j in range(nParticles):
            norm[i][j] = np.linalg.norm(xCopy[i][j] - x[nr])

    #normList = np.array(norm[0],norm[1])

    normSort = np.sort(norm, axis=1)
    #print(norm)
    normSort = np.array(norm).flatten()
    normSort = np.sort(normSort)
    #print(normSort)
    for i in range(k+1):
        if normSort[i] < r and normSort[i] != 0:
            #print("----------------")
            #print(normSort[i])
            #print(np.where(norm == normSort[i])[1][0])
            iii = np.where(norm == normSort[i])[1][0]
            posIndex.append(iii)
    #print(np.partition(norm,4)[:4])
    #for i in range(len(xCopy)):
        #for j in range(k+1):
            #if normSort[i][j] < r:
                #iii = np.where(norm[i] == normSort[i][j])
                #posIndex.append(iii[0])
    #print(list(dict.fromkeys(posIndex)))
    return list(dict.fromkeys(posIndex))

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

def getFlockIndex(position, L, r,k):
    flockIndex = []
    for i in range(len(position)):
        flockIndex.append(getParticleInRadius(position, i, L, r,k))
    return flockIndex

def P10(L,N,v,dt,noice,steps,r,k):


    [position, theta] = initRandomPositions(N,L)
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
        if i == 0 or i == 10 or i == 100 or i == 1000:
            #fig, ax = plt.subplots()
            #plotPeriodic(position, L)
            plotVoronoi(position, L)
            plt.title(f"configurations after iterations = {i},r={r},noice={noice},N={N}")
            plt.savefig(f"P10config;iter={i};r={r};noice={noice};N={N},k={k}".replace(".",","))
        fi[i] = getGlobalAlignment(velocity, v)
        cn[i] = globalClusteringCoefficient(position, L, r)
        flockIndex = getFlockIndex(position, L, r,k)
        theta = updateTheta(theta,flockIndex,noice,dt)
        velocity = getVelocity(theta, v)
        position = updatePosition(position, velocity, dt, L)

    #fig, ax = plt.subplots()
    plotVoronoi(position, L)
    plt.title(f"configurations after iterations = {steps},r={r},noice={noice},N={N}")
    plt.savefig(f"P10config;iter={i};r={r};noice={noice};N={N},k={k}".replace(".",","))
    plt.subplot()
    fig, ax = plt.subplots()
    #ax.plot(cn)
    ax.plot(fi)
    ax.plot(cn)
    plt.xlabel('timesteps t')
    plt.ylabel('fi,cn')
    plt.legend([r'$\psi$',r'$c$'])
    plt.savefig(f"P10fc;iter={steps};r={r};noice={noice};N={N},k={k}".replace(".",","))

    #plt.show()

