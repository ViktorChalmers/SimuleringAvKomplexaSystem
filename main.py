import numpy as np

import matplotlib
import random as random
import matplotlib.pyplot as plt

import matplotlib.animation as animation
from updateState import updateState
from initState import blinker,toad,beacon,glider,beehive,loaf,boat,rand,block,tub,foundStill
from OneDimensional import OneDimensional
from test import test

def main():
    nCols = 10
    nRows = 10
    #state = rand(size = [10,10],padding = 0)
    stilllife = "glider 3"
    state = rand([10,10],30)


    fig = plt.figure(figsize=(10,10))

    stateList = [state]
    initState = [state]
    im = plt.imshow(state, interpolation='none', aspect='auto', vmin=0, vmax=1)
    fps = 5
    nSeconds = 10

    newState = updateState(state,3)
    stateList.append(newState)

    for i in range(fps*nSeconds):
        newState = updateState(newState,3)
        stateList.append(newState)


    #state = np.zeros(100)
    #state[50] = 1
    #state = list(np.random.randint(low = 0,high=2,size=100))
    #print(state)
    #rule = 2
    #stateList = OneDimensional(state,rule = rule)


    def animate_func(i):
        if i % fps == 0:
            print('.', end='')
        im.set_array(stateList[i])
        plt.title(f"10x10_dead_4neigbours=alive, generation {i}")
        return [im]

    anim = animation.FuncAnimation(
        fig,
        animate_func,
        frames=nSeconds * fps,
        interval=1000 / fps,  # in ms
    )
    #title = f'One Dimensional, rule {rule}'
    #plt.title(title)

    #sav = f'One_Dimensional_Rule=,{rule}' + ".gif"
    #print("saving" + sav)
    sav = f'10x10_Modified_stable3.gif'
    #sav = f'Random_10x10_configuration.gif'
    anim.save(sav)
    plt.show()
    #anim.save('sine_wave.gif', writer='imagemagick')

if __name__ == '__main__':
    main()
