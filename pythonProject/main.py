import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm,trange



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

def playGame(state,N,reward,mu):
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

            r = np.random.rand()
            if r<mu:
                randomScore = np.random.randint(N+1)
                state[i,j] = randomScore
            else:
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
def P2(part="a", L = 10, N=7,mu=0, reward=[0,0.5,1,1.5],plot = False):
    R = reward[1]
    nrDef = 1
    if part == "a":
        initState = np.ones([L, L])*N
        mid = int(L/2)
        initState[mid,mid] = 0

    if part == "b":
        nrDef = 4
        initState = np.ones([L, L]) * N
        mid = int(L / 2)
        #initState[mid, mid] = 0
        initState[int(L/5), int(L/5)] = 0
        initState[2*int(L/5), 2*int(L/5)] = 0
        initState[3*int(L / 5), 3*int(L / 5)] = 0
        initState[4 * int(L / 5), 4 * int(L / 5)] = 0

    if part == "c":
        initState = np.ones([L, L])*0
        mid = int(L/2)
        initState[mid,mid] = 10

    if part == "d":
        nrDef = 9
        initState = np.ones([L, L])*0
        mid = int(L/2)
        initState[mid-1:mid+2,mid-1:mid+2]=np.ones([3,3])*10


    stateList = [np.copy(initState)]
    state = initState

    fps = 40
    nSeconds = 5
    #plt.imshow(state)
    #plt.show()
    for i in range(nSeconds*fps):
        #print(state)
        state = playGame(state, N, reward,mu)
        stateList.append(np.copy(state))
    #plt.imshow(state)
    #plt.show()
    #print(state)


    if plot:
        fig = plt.figure()

        im = plt.imshow(initState, interpolation='none', aspect='auto', vmin=0, vmax=1)
        plt.colorbar()
        def animate_func(i):
            if i % fps == 0:
                print('.', end='')
            im.set_array(stateList[i])
            #print(stateList[i]/10)
            plt.title(f"R = {R}, {nrDef} centered colab: Generation {i}")
            return [im]

        anim = animation.FuncAnimation(
            fig,
            animate_func,
            frames=nSeconds * fps,
            interval=1000 / fps,  # in ms
        )
        saveName = f'2{part}nrDef={nrDef};R={R}'.replace(".",",")+".gif"
        print("saving:"+saveName)
        #plt.show()
        anim.save(saveName, writer='imagemagick')
    return np.copy(state)
def P3(part):
    if part == 1:
        L=30
        S = 1.5
        R = 0.8
        N=7
        x2 = np.linspace(1,3,5)
        x = np.linspace(0.8,0.95,100)
        #print(x)
        y = np.zeros(len(x))
        for i in trange(len(x)):
            R=x[i]
            endState = P2(part="a", L=30, N=7, mu=0.01, reward=[0, R, 1, S], plot=False)
            y[i]=sum(sum(endState))/(L*L*N)

        plt.plot(x,y)
        plt.xlabel("R")
        #plt.title(f"Varying S nr of coop after 200 iterations")
        plt.legend(["varying R, S=1.5", "varying S, R=0.8"])
        plt.ylabel(f"normalized nr of cooperation")
        plt.savefig(f"varyingR")
    elif part == 2:
        L = 30
        S = 1.5
        R = 0.8
        N = 7
        x2 = np.linspace(1, 3, 5)
        x = np.linspace(1,3, 100)
        # print(x)
        y = np.zeros(len(x))
        for i in trange(len(x)):
            S = x[i]
            endState = P2(part="a", L=30, N=7, mu=0.01, reward=[0, R, 1, S], plot=False)
            y[i] = sum(sum(endState)) / (L * L * N)

        plt.plot(x, y)
        plt.xlabel("R")
        # plt.title(f"Varying S nr of coop after 200 iterations")
        plt.legend(["varying R, S=1.5", "varying S, R=0.8"])
        plt.ylabel(f"normalized nr of cooperation")
        plt.savefig(f"varyingR")





def P4(L = 10, N=7,mu=0, reward=[0,0.5,1,1.5],plot = False):
    R = reward[1]
    initState = np.random.randint(N+1,size=[L,L])
    #print(initState)

    stateList = [np.copy(initState)]
    state = initState

    fps = 5*10
    nSeconds = 10

    one = np.zeros(nSeconds*fps)
    two = np.zeros(nSeconds*fps)
    three = np.zeros(nSeconds*fps)
    four = np.zeros(nSeconds*fps)
    five = np.zeros(nSeconds*fps)
    six = np.zeros(nSeconds*fps)
    seven = np.zeros(nSeconds*fps)
    for i in trange(nSeconds * fps):
        state = playGame(state, N, reward, mu)
        stateList.append(np.copy(state))
        one[i] = (state == 1).sum()
        two[i] = (state == 2).sum()
        three[i] = (state == 3).sum()
        four[i] = (state == 4).sum()
        five[i] = (state == 5).sum()
        six[i] = (state == 6).sum()
        seven[i] = (state == 7).sum()

    plt.plot(one/(L*L))
    plt.plot(two/(L*L))
    plt.plot(three/(L*L))
    plt.plot(four/(L*L))
    plt.plot(five/(L*L))
    plt.plot(six/(L*L))
    plt.plot(seven/(L*L))
    plt.savefig("nrofPopulation")
    plt.show()
    plt.imshow(state)
    plt.show()
    plt.savefig("nrofPopulationState")

    if plot:
        fig = plt.figure()

        im = plt.imshow(initState, interpolation='none', aspect='auto', vmin=0, vmax=1)
        plt.colorbar()

        def animate_func(i):
            if i % fps == 0:
                print('.', end='')
            im.set_array(stateList[i]/N)
            # print(stateList[i]/10)
            plt.title(f"R = {R}, gen = {i}")
            return [im]

        anim = animation.FuncAnimation(
            fig,
            animate_func,
            frames=nSeconds * fps,
            interval=1000 / fps,  # in ms
        )
        saveName = f'13,4a;R={R}'.replace(".", ",") + ".gif"
        #print("saving:" + saveName)
        plt.show()
        anim.save(saveName, writer='imagemagick')
    return state
def P42():
    state = P4(L=30, N=7, mu=0, reward=[0, 0.5, 1, 1.5], plot=False)
    print(state)
    print((state == 3).sum())

if __name__ == '__main__':
    #P1(part="a",N=10,reward=[0,0.5,1,1.5],m=10)
    #P1(part="b",N=10,reward=[0,.01,1,10])
    #R = 0.88
    #R = 0.86
    #P2(part="d", L=30, N=7, reward=[0,R,1,1.5], plot = True)
    #R = 0.82
    #P2(part="a", L=30, N=7,mu=0.01, reward=[0,R,1,1.5], plot = True)
    #P3(part = 1)
    #P3(part = 2)
    #P4(L = 30, N=7,mu=0, reward=[0,0.5,1,1.5],plot = True)
    P42()


