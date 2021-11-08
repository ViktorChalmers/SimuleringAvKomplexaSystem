import numpy as np


def updateState(state):
    state = np.array(state)
    paddedState = np.pad(state, 1, mode='constant')
    nRows = np.size(state[0])
    nCols = np.size(state[1])
    sum = np.zeros([nRows,nCols])

    sum = calculateSum(state)

    newState = np.zeros([nRows,nCols])
    for i in range(nRows):
        for j in range(nCols):
            if state[i][j] == 1 and sum[i][j] == 2:
                newState[i][j] = 1
            if state[i][j] == 1 and sum[i][j] == 3:
                newState[i][j] = 1
            if state[i][j] == 0 and sum[i][j] == 3:
                    newState[i][j] = 1

    return newState

def calculateSum(state,type = "periodic"):
    if type =="periodic":
        fRow = np.copy(state[0, :])
        lRow = np.copy(state[-1, :])

        fCol = np.copy(state[:, 0])
        lCol = np.copy(state[:, -1])

        paddedState = np.pad(state, 1, mode='constant')
        paddedState[0, 1:-1] = lRow
        paddedState[-1, 1:-1] = fRow
        paddedState[1:-1, 0] = lCol
        paddedState[1:-1, -1] = fCol
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
    return sum
