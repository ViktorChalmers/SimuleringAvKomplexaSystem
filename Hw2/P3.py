import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from functions import initRandomPositions,plotPeriodic

def P3():
    # make up data points
    N=10
    L=5
    points = initRandomPositions(N,L)


    # compute Voronoi tesselation
    #vor = Voronoi(points)
    # plot
    #voronoi_plot_2d(vor)
    plotPeriodic(points, L)
    #print(vor.regions)
    #plt.show()