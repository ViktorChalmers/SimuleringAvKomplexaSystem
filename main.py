import numpy as np

import matplotlib
import random as random
import matplotlib.pyplot as plt

import matplotlib.animation as animation
from updateState import updateState
from initState import blinker,toad,beacon,glider,beehive,loaf,boat,rand
from OneDimensional import OneDimensional

def main():
    nCols = 25
    nRows = 25
    state = rand(size = [5,5],padding = 50)

    fig = plt.figure(figsize=(10,10))

    stateList = [state]
    initState = [state]
    im = plt.imshow(state, interpolation='none', aspect='auto', vmin=0, vmax=1)
    fps = 20
    nSeconds = 10

    newState = updateState(state)
    stateList.append(newState)

    for i in range(fps*nSeconds):
        newState = updateState(newState)
        stateList.append(newState)


    state = np.zeros(100)
    state[50] = 1

    state = list(np.random.randint(low = 0,high=1,size=100))
    print(state)

    rule = 184
    stateList = OneDimensional(state,rule = rule)


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
    title = f'One Dimensional, rule {rule}'
    plt.title(title)

    sav = f'One_Dimensional_Rule=,{rule}' + ".gif"
    print("saving" + sav)
    anim.save(sav)
    #plt.show()
    #anim.save('sine_wave.gif', writer='imagemagick')

if __name__ == '__main__':
    main()
