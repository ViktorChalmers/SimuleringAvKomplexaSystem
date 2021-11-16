import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d,ConvexHull
from functions import initRandomPositions,plotPeriodic,expandPeriodic

def voronoiArea(vor,nr,plott=False):
    index = nr
    vorIndex = vor.point_region[index]
    reg1 = vor.regions[vorIndex]
    ver = vor.vertices[reg1]
    if plott==True:
        plt.plot(ver[:, 0], ver[:, 1], "o")
    area = ConvexHull(vor.vertices[reg1]).volume
    return area

def globalClusteringCoefficient(position,L,r):
    N = len(position[:,0])
    copy = expandPeriodic(position, L)
    expandPositions = np.copy(position)

    for i in range(len(copy)):
        expandPositions = np.append(expandPositions, copy[i], axis=0)

    vor = Voronoi(expandPositions)
    area = np.zeros(len(position))
    for i in range(len(position)):
        area[i] = voronoiArea(vor, i)

    c = 0
    for i in range(len(position)):
        if area[i] < np.pi * r ** 2:
            c += 1
            #circle = plt.Circle((position[i]), r, fill=False)
            #ax.add_patch(circle)
    c = c / N
    return c

def P3(N=4,L=4,r=1):
    [position, theta] = initRandomPositions(N, L)
    copy = expandPeriodic(position, L)
    expandPositions = np.copy(position)

    for i in range(len(copy)):
        expandPositions = np.append(expandPositions,copy[i],axis=0)

    vor = Voronoi(expandPositions)
    voronoi_plot_2d(vor)
    area = np.zeros(len(position))
    for i in range(len(position)):
        area[i] = voronoiArea(vor, i)


    rectangle = plt.Rectangle((-L / 2, -L / 2), L, L, fill=False, ec="red")
    plt.xlim(-3 * L / 2, 3 * L / 2)
    plt.ylim(-3 * L / 2, 3 * L / 2)
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_patch(rectangle)

    c=0
    for i in range(len(position)):
        if area[i]<np.pi*r**2:
            c+=1
            circle = plt.Circle((position[i]), r, fill=False)
            ax.add_patch(circle)
    c = c/N
    print(c)
    coeff = globalClusteringCoefficient(position, L,r)
    print(coeff)
    plt.show()