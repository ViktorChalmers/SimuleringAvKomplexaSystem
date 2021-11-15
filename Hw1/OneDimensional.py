import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def pattern(state):
    pattern = np.zeros([len(state)-2,3])

    for i in range(1,len(state)-1):
        pattern[i-1,:] = [state[i-1],state[i],state[i+1]]
    return pattern

def update(state,rule=184):
    pat = pattern(state)
    nextState = np.zeros(len(state))
    if rule == 184:
        for i in range(len(pat)):
            if np.array_equal(pat[i,:],[1, 1, 1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [1, 0, 1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [1,0,0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,1,1]):
                nextState[i+1] = 1
    elif rule == 90:
        for i in range(len(pat)):
            if np.array_equal(pat[i,:],[1, 1, 0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [1, 0, 0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,1,1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,0,1]):
                nextState[i+1] = 1
    elif rule == 30:
        for i in range(len(pat)):
            if np.array_equal(pat[i,:],[1, 0, 0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0, 1, 1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,1,0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,0,1]):
                nextState[i+1] = 1
    elif rule == 110:
        for i in range(len(pat)):
            if np.array_equal(pat[i,:],[1, 1, 0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [1, 0, 1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,1,1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,1,0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,0,1]):
                nextState[i+1] = 1
    elif rule == 1:
        for i in range(len(pat)):
            if np.array_equal(pat[i,:],[1, 1, 0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [1, 0, 1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,1,1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,1,0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,0,1]):
                nextState[i+1] = 0
    elif rule == 2:
        for i in range(len(pat)):
            if np.array_equal(pat[i,:],[1, 1, 0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [1, 0, 1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,1,1]):
                nextState[i+1] = 0
            if np.array_equal(pat[i, :], [0,1,0]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [0,0,1]):
                nextState[i+1] = 1
            if np.array_equal(pat[i, :], [1,0,0]):
                nextState[i+1] = 1
    return nextState

def OneDimensional(state,rule = 184):

    nextState = state
    nGenerations = len(state)
    stateListing = [np.zeros([nGenerations,len(state)])]

    stateList = np.zeros([nGenerations,len(state)])
    stateList[0,:] = state
    for i in range(1,nGenerations):
        nextState = update(nextState,rule)
        stateList[i,:] = nextState
        stateListing.append(np.copy(stateList))

    return stateListing

