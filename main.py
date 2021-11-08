import numpy as np

import matplotlib
import random as random
import matplotlib.pyplot as plt

import matplotlib.animation as animation
from updateState import updateState,checkState
from initState import blinker,toad,beacon,glider,beehive,loaf,boat,rand
from OneDimensional import OneDimensional

def main():
    nCols = 25
    nRows = 25
    loop = True
    fig = plt.figure(figsize=(10, 10))

    state = glider()
    state = np.array([
        [0,1,1],
        [1, 0,1],
        [0, 1, 0]
    ])
    state = np.pad(state,10)

    stateList = [state]
    initState = [state]
    im = plt.imshow(state, interpolation='none', aspect='auto', vmin=0, vmax=1)
    fps = 10
    nSeconds = 10

    newState = updateState(state)
    checkState(state,newState)
    stateList.append(newState)

    for i in range(fps*nSeconds):
        newState = updateState(newState)
        stateList.append(newState)

    #state = np.zeros(100)
    #state[50] = 1
    #state = list(np.random.randint(low=0, high=2, size=100))
    #print(state)
    #stateList = OneDimensional(state,rule = 184)


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

if __name__ == '__main__':
    main()
