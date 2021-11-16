import numpy as np
import matplotlib.pyplot as plt

def periodicBoundary(x, L):
    for i in range(len(x[:, 0])):
        for j in range(len(x[0, :])):
            if x[i, j] < -L / 2:
                x[i, j] = x[i, j] + L
            elif x[i, j] > L / 2:
                x[i, j] = x[i, j] - L
    return x


def initRandomPositions(N, L):
    x = np.random.rand(N, 2) * L - L / 2
    theta = np.random.rand(N)*2*np.pi
    return [periodicBoundary(x, L), theta]


def displaceParticles(x, step, L):
    x[:, 0] = x[:, 0] + step
    x[:, 1] = x[:, 1] + step
    return periodicBoundary(x, L)


def plotPeriodic(x, L,nr=0,r=0):
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

    plt.plot(x[:, 0], x[:, 1], "o")
    plt.plot(xCopyDown[:, 0], xCopyDown[:, 1], "*")
    plt.plot(xCopyUp[:, 0], xCopyUp[:, 1], "*")
    plt.plot(xCopyRight[:, 0], xCopyRight[:, 1], "*")
    plt.plot(xCopyLeft[:, 0], xCopyLeft[:, 1], "*")
    plt.plot(xCopyDiag1[:, 0], xCopyDiag1[:, 1], "*")
    plt.plot(xCopyDiag2[:, 0], xCopyDiag2[:, 1], "*")
    plt.plot(xCopyDiag3[:, 0], xCopyDiag3[:, 1], "*")
    plt.plot(xCopyDiag4[:, 0], xCopyDiag4[:, 1], "*")

    rectangle = plt.Rectangle((-L / 2, -L / 2), L, L, fill=False, ec="red")
    plt.xlim(-3 * L / 2, 3 * L / 2)
    plt.ylim(-3 * L / 2, 3 * L / 2)
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_patch(rectangle)
    plt.xlim(-3 * L / 2, 3 * L / 2)
    plt.ylim(-3 * L / 2, 3 * L / 2)

    if r != 0:
        circle1 = plt.Circle((x[nr]), r, fill=False)
        ax.add_patch(circle1)
    return [fig, ax]


def getParticleInRadius(x, nr, L, r):
    nParticles = len(x[:, 0])
    norm = np.zeros([len(x[:, 0]), 1])
    posIndex = []

    for i in range(nParticles):
        norm[i] = np.linalg.norm(x[i] - x[nr])

    for i in range(nParticles):
        np.append(posIndex, i)
        if norm[i] < r and norm[i] != 0:
            posIndex.append(i)

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

    xCopy = [xCopyDown, xCopyUp, xCopyRight, xCopyLeft,
             xCopyDiag1, xCopyDiag2, xCopyDiag3, xCopyDiag4]

    norm = np.zeros([len(xCopy), nParticles])
    for i in range(len(xCopy)):
        for j in range(nParticles):
            norm[i][j] = np.linalg.norm(xCopy[i][j] - x[nr])

    for i in range(len(xCopy)):
        for j in range(nParticles):
            if norm[i][j] < r:
                posIndex.append(j)
    return posIndex

def getGlobalAlignment(x,nr,r,L):
    indexRadius = getParticleInRadius(x,nr,L,r)
    align = len(indexRadius)/len(x)
    return align