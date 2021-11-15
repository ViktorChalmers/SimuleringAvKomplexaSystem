import numpy as np
import matplotlib.pyplot as plt
import time

def initPlot(dim = [10,10]):
    print(dim[1])
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    #plt.title("Sports Watch Data")
    #plt.xlabel("Average Pulse")
    #plt.ylabel("Calorie Burnage")

    #plt.plot(x, y)
    #plt.axis([0, dim[1], 0, dim[0]])
    #plt.xticks([1,2,3,4,5,6,7,8,9,10])
    #plt.yticks([1,2,3,4,5,6,7,8,9,10])
    #plt.grid()
    state = np.zeros([10,10])
    state[1][0] = 1
    plt.imshow(state)
    plt.show()
    #time.sleep(1)
    state[1][0] = 0
    plt.imshow(state)
    plt.show()
    #plotSquare(position = [1,1])

def plotSquare(position = [1,1]):
    print("sf")
    i = position[0]
    j = position[1]
    plt.fill_between([i, i+1],[j,j], [j+1, j+1])
