import numpy as np
from updateState import calculateSum
import matplotlib.pyplot as plt
from matplotlib import animation

def initState(nRows,nCols,p=0.5):
    state=np.zeros([nRows,nCols])
    for i in range(nRows):
        for j in range(nCols):
            r = np.random.rand()
            if r<p:
                state[i,j] = 1

    return state


def updateMajorityState(state):
    [nRows,nCols] = np.shape(state)
    sum = calculateSum(state)
    nextState = np.copy(state)
    for i in range(nRows):
        for j in range(nCols):
            if sum[i,j] == 0 or sum[i,j] == 1 or sum[i,j] == 2 or sum[i,j] == 3:
                nextState[i,j] = 0
            elif sum[i,j] == 5 or sum[i,j] == 6 or sum[i,j] == 7 or sum[i,j] == 8:
                nextState[i,j] = 1
    return nextState

nRows = 100
nCols = 100
p = 0.5
initState = initState(nRows,nCols,p)
state = np.copy(initState)
stateList = [state]

fps = 10
nSeconds = 5
stable = [0]
for i in range(fps * nSeconds):
    newState = updateMajorityState(state)
    stateList.append(state)
    if np.array_equal(newState,state):
        stable.append(i)
        state = np.copy(newState)
    else:
        state = np.copy(newState)

fig = plt.figure()
im = plt.imshow(initState)
st = 0
def animate(i):
    if i % fps == 0:
        print('.', end='')
    if stable[1]:
        st = stable[1]
    plt.title(f'Majority Rule P=0,{p * 10:.0f}, gen = {i}, stable at gen = {st}')
    #title = f'Majority Rule P=0,{p * 10:.0f}, stable {st}'
    #plt.title(title)
    im.set_array(stateList[i])
    return [im]

anim = animation.FuncAnimation(
        fig,
        animate,
        frames=nSeconds * fps,
        interval=1000 / fps,  # in ms
    )


sav = f'Majority_Rule_P=0,{p*10:.0f}' + ".gif"
print("saving" + sav)
anim.save(sav)
#plt.show()
