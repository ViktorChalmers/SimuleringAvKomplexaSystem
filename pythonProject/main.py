import numpy as np
import matplotlib.pyplot as plt



def getStats(N,n,m,reward):#return stats for player with strategy n
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

def playGame(state,N,reward):
    expandedState = expandPeriodic(state)
    print(state)
    for i in range(len(state)):
        for j in range(len(state)):
            index = np.array([i,j])
            [selfStrategy, neigborStrategy] = getVonNeumannNeighbors(expandedState,index)
            print(neigborStrategy)
            stats = np.zeros(4)
            for k in range(4):
                stats[k] = getStats(N, selfStrategy, neigborStrategy[k], reward)
            print(stats)
            minNeigbourIndex = np.argmin(stats)
            if getStats(N, minNeigbourIndex, selfStrategy,  reward) > stats[minNeigbourIndex]:
                state[index[0],index[1]] = neigborStrategy[minNeigbourIndex]
    print(state)


def P2(part="a", L = 10, N=10, reward=[0,0.5,1,1.5]):
    if part == "a":
        state = np.ones([L, L])*N
        #state = np.random.randint(10,size=[L,L])
        mid = int(L/2)
        state[mid,mid] = 0
        state = playGame(state,N,reward)

if __name__ == '__main__':
    #P1(part="a",N=10,reward=[0,0.5,1,1.5],m=10)
    #P1(part="b",N=10,reward=[0,.01,1,10])
    R = 0.5
    #P2(part="a", L=3, N=10, reward=[0,R,1,1.5])
    print(getStats(N=10, n=10, m=10, reward=[0,R,1,1.5]))
