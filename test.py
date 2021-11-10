import numpy as np
from updateState import translate,calculateSum,checkState,updateState
import matplotlib.pyplot as plt
from initState import blinker,toad,beacon,glider,beehive,loaf,boat,rand

def test(size = [3,3]):
    loop = True
    fig = plt.figure(figsize=(10, 10))
    while(loop):

        nRows = size[0]
        nCols = size[1]


        state = rand([nRows,nCols],nRows*3)
        #state = np.array([
        #    [0, 0, 0],
        #    [0, 1, 0],
        #    [1, 1, 1],
        #])




        stateList = [state]
        initState = [state]
        im = plt.imshow(state, interpolation='none', aspect='auto', vmin=0, vmax=1)
        fps = 10
        nSeconds = 3

        newState = updateState(state)
        checkState(state,newState)
        stateList.append(newState)
        comState = np.zeros([10,10])
        for i in range(fps*nSeconds):

            if i == 15:
                comState = np.copy(newState)
            newState = updateState(newState)
            stateList.append(newState)
            if np.all(newState==0):
                continue
            if(checkState(comState, newState)):
                print(i+2)
                print(state)
                loop = False
                plt.imshow(state)
                plt.show()
                break
    return state