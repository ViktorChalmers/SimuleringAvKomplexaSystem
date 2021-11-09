import numpy as np
from updateState import translate,calculateSum,checkState,updateState
import matplotlib.pyplot as plt
from initState import blinker,toad,beacon,glider,beehive,loaf,boat,rand

loop = True
fig = plt.figure(figsize=(10, 10))
while(loop):


    state = rand([5,5],15)
    #state = np.array([
    #    [0, 0, 0],
    #    [0, 1, 0],
    #    [1, 1, 1],
    #])




    stateList = [state]
    initState = [state]
    im = plt.imshow(state, interpolation='none', aspect='auto', vmin=0, vmax=1)
    fps = 10
    nSeconds = 2

    newState = updateState(state)
    checkState(state,newState)
    stateList.append(newState)

    for i in range(fps*nSeconds):
        newState = updateState(newState)
        stateList.append(newState)
        if(checkState(state, newState)):
            print(i+2)
            print(state)
            loop = False
            plt.imshow(state)
            plt.show()
            break