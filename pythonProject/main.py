import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def getScore(N,n,m,reward):#return stats for player with strategy n
    T = reward[0]
    R = reward[1]
    P = reward[2]
    S = reward[3]
    stats = 0
    for i in range(N):
        if i <= n - 1 and i <= m - 1:
            stats += R
        elif n < m:
            stats += T
            stats += P * (N - i - 1)
            break
        elif n == m:
            stats += P * (N - i)
            break
        else:
            stats += S
            stats += P * (N - i - 1)
            break
    return stats
def P1(part,N,reward,m=0,n=0):
    T = reward[0]
    R = reward[1]
    P = reward[2]
    S = reward[3]
    if part == "a":

        reward = [T,R,P,S]
        summ = np.zeros(N)
        for n in range(N):
            summ[n] = getStats(N, n, m,reward)
        plt.plot(summ, "o")
        plt.axvline(x=m)
        plt.title(f"m={m}")
        plt.ylabel("Years in prison")
        plt.xlabel("n")
        plt.savefig(f"1a;m={m}")
        plt.show()
    if part == "b":
        reward = [T,R,P,S]
        summ = np.zeros([N, N])
        for n in range(N):
            for m  in range(N):
                summ[n,m] = getStats(N, n, m,reward)

        plt.imshow(summ)
        ax = plt.gca()
        ax.invert_yaxis()
        plt.colorbar()
        plt.xlabel("sd")
        plt.xlabel("sd")
        plt.title(f"N = {N}, reward = {reward}")
        plt.savefig(f"1b;N={N},reward={reward}".replace(".",","))
        plt.show()

def expandPeriodic(state):
    exp = np.pad(state, 1, 'constant')
    exp[0, 1:-1] = np.copy(state[-1])
    exp[-1, 1:-1] = np.copy(state[0])
    exp[1:-1, 0] = np.copy(state[:, -1])
    exp[1:-1, -1] = np.copy(state[:, 0])

    exp[0, 0] = np.copy(state[-1, -1])
    exp[-1, 0] = np.copy(state[0, -1])
    exp[0,-1] = np.copy(state[-1, 0])
    exp[-1, -1] = np.copy(state[0, 0])

    return exp

def getVonNeumannNeighbors(expandedState,index):
    index = index+1

    #print(expandedState)
    self = expandedState[index[0],index[1]]
    up = expandedState[index[0]-1,index[1]]
    down = expandedState[index[0]+1,index[1]]
    left = expandedState[index[0],index[1]-1]
    right = expandedState[index[0],index[1]+1]
    list = np.array([up, down, left, right])
    #print(list)
    return [self, list]

def getStats(state,N,reward):
    expandedState = expandPeriodic(state)
    stats = np.zeros([len(state), len(state)])
    for i in range(len(state)):
        for j in range(len(state)):
            index = np.array([i,j])
            [selfStrategy, neigborStrategy] = getVonNeumannNeighbors(expandedState,index)
            #print(neigborStrategy)
            score = 0
            for k in range(4):
                score = score + getScore(N, selfStrategy, neigborStrategy[k], reward)
            stats[i,j] = score
    return stats

def playGame(state,N,reward):
    stats = getStats(state,N,reward)

    expandedStats = expandPeriodic(stats)
    expandedState = expandPeriodic(state)
    for i in range(len(state)):
        for j in range(len(state)):
            index = np.array([i, j])
            [selfScore, neigborScore] = getVonNeumannNeighbors(expandedStats,index)
            np.argmin(neigborScore)
            minIndex = np.where(neigborScore == neigborScore.min())[0]
            minIndex = minIndex[np.random.randint(len(minIndex))]



            if neigborScore[minIndex] < selfScore:

                if minIndex == 0:
                    state[i, j] = expandedState[i-1+1, j+1]

                if minIndex == 1:
                    state[i, j] = expandedState[i+1+1, j+1]

                if minIndex == 2:
                    state[i, j] = expandedState[i+1, j-1+1]

                if minIndex == 3:
                    state[i, j] = expandedState[i+1, j+1+1]

    return state
def P2(part="a", L = 10, N=9, reward=[0,0.5,1,1.5],plot = False):

    if part == "a":
        initState = np.ones([L, L])*N
        mid = int(L/2)
        initState[mid,mid] = 0
        stateList = [initState]
        state = initState

        fps = 10
        nSeconds = 3
        for i in range(fps*nSeconds):
            state = playGame(state, N, reward)
            stateList.append(np.copy(state))
            #plt.imshow(stateList[i])
            #plt.show()
    if plot:
        fig = plt.figure()

        #stateList = [state]
        #initState = [state]
        im = plt.imshow(initState, interpolation='none', aspect='auto', vmin=0, vmax=1)
        fps = 5
        nSeconds = 5
        def animate_func(i):
            if i % fps == 0:
                print('.', end='')
            im.set_array(stateList[i])
            plt.title(f"R = {R}, one centered defected: Generation {i}")
            return [im]

        anim = animation.FuncAnimation(
            fig,
            animate_func,
            frames=nSeconds * fps,
            interval=1000 / fps,  # in ms
        )
        saveName = f'2a;R={R}'.replace(".",",")+".gif"
        print("saving:"+saveName)
        #plt.show()
        anim.save(saveName, writer='imagemagick')


if __name__ == '__main__':
    #P1(part="a",N=10,reward=[0,0.5,1,1.5],m=10)
    #P1(part="b",N=10,reward=[0,.01,1,10])
    #R = 0.88
    #P2(part="a", L=30, N=7, reward=[0,R,1,1.5], plot = True)
    Rt = 0.88
    for r in range(13):
        R = Rt+r/100
        P2(part="a", L=30, N=7, reward=[0, R, 1, 1.5], plot=True)

