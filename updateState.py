import numpy as np


def updateState(state,nr=1):
    state = np.array(state)
    paddedState = np.pad(state, 1, mode='constant')
    nRows = np.size(state[0])
    nCols = np.size(state[1])
    sum = np.zeros([nRows,nCols])

    sum = calculateSum(state)

    newState = np.zeros([nRows,nCols])
    if(nr==1):
        for i in range(nRows):
            for j in range(nCols):
                if state[i][j] == 1 and sum[i][j] == 2:
                    newState[i][j] = 1
                if state[i][j] == 1 and sum[i][j] == 3:
                    newState[i][j] = 1
                if state[i][j] == 0 and sum[i][j] == 3:
                        newState[i][j] = 1
    elif(nr==2):
        for i in range(nRows):
            for j in range(nCols):
                if state[i][j] == 1 and sum[i][j] == 2:
                    newState[i][j] = 0 #changed
                if state[i][j] == 1 and sum[i][j] == 3:
                    newState[i][j] = 1
                if state[i][j] == 0 and sum[i][j] == 3:
                        newState[i][j] = 1
    elif (nr == 3):
        for i in range(nRows):
            for j in range(nCols):
                if state[i][j] == 1 and sum[i][j] == 2:
                    newState[i][j] = 1
                if state[i][j] == 1 and sum[i][j] == 3:
                    newState[i][j] = 1
                if state[i][j] == 1 and sum[i][j] == 4:
                        newState[i][j] = 1 #added
                if state[i][j] == 1 and sum[i][j] == 5:
                        newState[i][j] = 0 # added
                if state[i][j] == 0 and sum[i][j] == 5:
                    newState[i][j] = 1 #changed
                if state[i][j] == 0 and sum[i][j] == 4:
                    newState[i][j] = 1 # added

    return newState

def calculateSum(state,type = "periodic"):
    if type =="periodic":
        fRow = np.copy(state[0, :])
        lRow = np.copy(state[-1, :])

        fCol = np.copy(state[:, 0])
        lCol = np.copy(state[:, -1])

        paddedState = np.pad(state, 1, mode='constant')
        paddedState[1:-1, 0] = np.copy(state[:, -1])
        paddedState[1:-1, -1] = np.copy(state[:, 0])
        paddedState[0, 1:-1] = np.copy(state[-1, :])
        paddedState[-1, 1:-1] = np.copy(state[0, :])
        paddedState[0, 0] = np.copy(state[-1, -1])
        paddedState[-1, -1] = np.copy(state[0, 0])
        paddedState[0, -1] = np.copy(state[-1, 0])
        paddedState[-1, 0] = np.copy(state[0, -1])
        #print("Periodic")
    else:
        #print("Padded")
        state = np.array(state)
        paddedState = np.pad(state, 1, mode='constant')

    nRows = np.size(state[0])
    nCols = np.size(state[1])
    sum = np.zeros([nRows, nCols])


    for i in range(1, nRows):
        for j in range(1, nCols):

            if (paddedState[i - 1, j - 1] == 1):
                sum[i - 1][j - 1] = sum[i - 1][j - 1] + 1

            if (paddedState[i - 1, j] == 1):
                sum[i - 1][j - 1] = sum[i - 1][j - 1] + 1

            if (paddedState[i - 1, j + 1] == 1):
                sum[i - 1][j - 1] = sum[i - 1][j - 1] + 1

            if (paddedState[i, j - 1] == 1):
                sum[i - 1][j - 1] = sum[i - 1][j - 1] + 1

            if (paddedState[i, j + 1] == 1):
                sum[i - 1][j - 1] = sum[i - 1][j - 1] + 1

            if (paddedState[i + 1, j - 1] == 1):
                sum[i - 1][j - 1] = sum[i - 1][j - 1] + 1

            if (paddedState[i + 1, j] == 1):
                sum[i - 1][j - 1] = sum[i - 1][j - 1] + 1

            if (paddedState[i + 1, j + 1] == 1):
                sum[i - 1][j - 1] = sum[i - 1][j - 1] + 1

    [nRows, nCols] = np.shape(state)
    sum = np.zeros([nRows, nCols])

    for i in range(nRows):
        for j in range(nCols):
            sum[i, j] = np.sum(paddedState[i, j:j + 3]) + \
                        np.sum(paddedState[i + 2, j:j + 3]) + \
                        paddedState[i + 1, j] + \
                        paddedState[i + 1, j + 2]
    return sum

def translate(state,sx,sy):
    state = np.roll(state, sy, axis=0)
    state = np.roll(state, sx, axis=1)
    return state
def checkState(state1,state2):
    direction = np.array([
        [0 ,0],
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
    ])
    for i in direction:
        if np.array_equal(state2,translate(state1,i[0],i[1])):
            print('translated direction',  i)
            return True
            break
    return False