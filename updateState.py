import numpy as np

def updateState(state):
    state = np.array(state)
    paddedState = np.pad(state, 1, mode='constant')
    nRows = np.size(state[0])
    nCols = np.size(state[1])
    sum = np.zeros([nRows,nCols])

    for i in range(1,nRows):
        for j in range(1,nCols):

            if (paddedState[i - 1,j - 1] == 1):
                sum[i-1][j-1] = sum[i-1][j-1] + 1

            if (paddedState[i - 1, j] == 1):
                sum[i-1][j-1] = sum[i-1][j-1] + 1

            if (paddedState[i - 1, j + 1] == 1):
                sum[i-1][j-1] = sum[i-1][j-1] + 1

            if (paddedState[i, j - 1] == 1):
                sum[i-1][j-1] = sum[i-1][j-1] + 1

            if (paddedState[i, j + 1] == 1):
                sum[i-1][j-1] = sum[i-1][j-1] + 1

            if (paddedState[i + 1, j - 1] == 1):
                sum[i-1][j-1] = sum[i-1][j-1] + 1

            if (paddedState[i + 1, j] == 1):
                sum[i-1][j-1] = sum[i-1][j-1] + 1

            if (paddedState[i + 1, j + 1] == 1):
                sum[i-1][j-1] = sum[i-1][j-1] + 1

    newState = np.zeros([nRows,nCols])
    for i in range(nRows):
        for j in range(nCols):
            if state[i][j] == 1 and sum[i][j] == 2:
                newState[i][j] = 1
            if state[i][j] == 1 and sum[i][j] == 3:
                newState[i][j] = 1
            if state[i][j] == 0 and sum[i][j] == 3:
                    newState[i][j] = 1


    #print(paddedState)
    #paddedState = paddedState[1:10,1:10]
    #print(paddedState)



    return newState