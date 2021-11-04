import numpy as np

import matplotlib
import random as random
import matplotlib.pyplot as plt

import matplotlib.animation as animation
from updateState import updateState

def main():
    nCols = 100
    nRows = 100
    state = np.random.randint(2, size=[nRows,nCols])

    fig = plt.figure(figsize=(10,10))
    #state = np.zeros([nRows, nCols])
    #state[1][2] = 1
    #state[2][2] = 1
    #state[3][2] = 1

    state[6][6] = 1
    state[5][5] = 1
    state[4][5] = 1
    state[4][6] = 1
    state[4][7] = 1
    #state[6][7] = 1
    stateList = [state]
    im = plt.imshow(state, interpolation='none', aspect='auto', vmin=0, vmax=1)
    fps = 5
    nSeconds = 10
    #print(state)
    newState = updateState(state)
    stateList.append(newState)
    #print(newState)
    for i in range(100):
        newState = updateState(newState)
        stateList.append(newState)



    #print(stateList)
    #def update(state):

    def animate_func(i):
        if i % fps == 0:
            print('.', end='')

        im.set_array(stateList[i])
        return [im]

    anim = animation.FuncAnimation(
        fig,
        animate_func,
        frames=nSeconds * fps,
        interval=1000 / fps,  # in ms
    )
    plt.show()
    #anim.save('sine_wave.gif', writer='imagemagick')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


