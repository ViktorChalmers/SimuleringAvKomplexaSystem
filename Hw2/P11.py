from functions import initRandomPositions, plotPeriodic, getVelocity, getGlobalAlignment,\
    globalClusteringCoefficient,plotVoronoi,periodicBoundary
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange

def getParticlesInCone(x, nr, L, r, theta, alpha):
    plt.plot(x[nr,0]+r*np.cos(theta[nr]+alpha/2),x[nr,1]+r*np.sin(theta[nr]+alpha/2),"*")
    posIndex = [nr]
    plt.plot(x[nr, 0] + r * np.cos(theta[nr] - alpha / 2), x[nr, 1] + r * np.sin(theta[nr] - alpha / 2), "*")
    a = np.array([np.cos(theta[nr]), np.sin(theta[nr])])

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
    start = np.copy(x)
    xCopy = [start, xCopyDown, xCopyUp, xCopyRight, xCopyLeft,
             xCopyDiag1, xCopyDiag2, xCopyDiag3, xCopyDiag4]

    gamma = np.zeros([len(xCopy), len(x)])
    b = []

    for i in range(len(xCopy)):
        b.append(xCopy[i] - x[nr])
        for j in range(len(x)):
            if j != nr:

                gamma[i][j] = np.arccos((np.dot(a, b[i][j])) / (np.linalg.norm(a) * np.linalg.norm(b[i][j])))
            else:
                gamma[i][j] = 0

    for i in range(len(xCopy)):
        for j in range(len(x)):
            if np.abs(gamma[i][j])<alpha/2 and np.linalg.norm(xCopy[i][j]-x[nr])<r:

                posIndex.append(j)


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

def getFlockIndex(position, L, r,theta, alpha):
    flockIndex = []
    for i in range(len(position)):
        flockIndex.append(getParticlesInCone(position, i, L, r,theta, alpha))
    return flockIndex

def P11test(L,N,v,dt,noice,steps,r,alpha):
    boundaryLength = L
    flockingRadius = r
    particleNr = 1
    nParticles = N

    [position, theta] = initRandomPositions(nParticles, boundaryLength)


    posIndex = getParticlesInCone(position,particleNr,L = boundaryLength,r = flockingRadius,theta=theta, alpha = alpha)

    ret = np.zeros([len(posIndex), 2])
    for i in range(len(posIndex)):
        ret[i] = position[posIndex[i]]

    [fig,ax] = plotPeriodic(position, boundaryLength)
    plt.plot(ret[:, 0], ret[:, 1], "*",color="black")
    plt.plot(position[particleNr,0]+L/10*np.cos(theta[particleNr]),position[particleNr,1]+L/10*np.sin(theta[particleNr]),"*",color="purple")
    plt.title(f"Theta = {theta[particleNr]*360/(np.pi*2):.2f}")
    circle1 = plt.Circle((position[particleNr]), flockingRadius, fill=False)
    ax.add_patch(circle1)
    #print(posIndex)
    plt.show()


def P11(L,N,v,dt,noice,steps,r,alpha):


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
            plt.savefig(f"P11config;iter={i};r={r};noice={noice};N={N},alpha={alpha}:0.3f".replace(".",","))
        fi[i] = getGlobalAlignment(velocity, v)
        cn[i] = globalClusteringCoefficient(position, L, r)
        flockIndex = getFlockIndex(position, L, r,theta, alpha)
        theta = updateTheta(theta,flockIndex,noice,dt)
        velocity = getVelocity(theta, v)
        position = updatePosition(position, velocity, dt, L)

    #fig, ax = plt.subplots()
    plotVoronoi(position, L)
    plt.title(f"configurations after iterations = {steps},r={r},noice={noice},N={N}")
    plt.savefig(f"P11config;iter={i};r={r};noice={noice};N={N},alpha={alpha}".replace(".",","))
    plt.subplot()
    fig, ax = plt.subplots()
    #ax.plot(cn)
    ax.plot(fi)
    ax.plot(cn)
    plt.xlabel('timesteps t')
    plt.ylabel('fi,cn')
    plt.legend([r'$\psi$',r'$c$'])
    plt.savefig(f"P11fc;iter={steps};r={r};noice={noice};N={N},alpha={alpha}".replace(".",","))

    #plt.show()