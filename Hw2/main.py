import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm,trange
import time

def update(x0,pl=1):
    p = np.random.rand()
    if p<0.5:
        x = x0 + pl
    else:
        x = x0 - pl
    return x

def P1(nSteps,sigma,dt,N=10000):

    rel = np.zeros(N)
    for j in trange(N):
        x=0
        for i in range(nSteps):
            x = update(x)
        rel[j] = x
    return(rel)

def P2(nSteps,sigma,dt,L,N=10000):
    pl = round(sigma*np.sqrt(0.01),5)
    rel = np.zeros(N)
    for j in trange(N):
        #print(j)
        x=0
        for i in range(nSteps):
            x = update(x,pl)
            if x<-L/2:
                x = -L-x
            elif x > L / 2:
                x = L - x
        rel[j] = x
    return(rel)

def plotHist(rel,sigma,dt,nSteps):
    print(f"Standard deviation = {np.std(rel):.3f}, sigma*sqrt(2*nSteps*dt) = {sigma*np.sqrt(2*nSteps*dt):.3f}, T = {dt*nSteps}")
    plt.hist(rel,histtype="step", label="Line 1")
    plt.title(f"Standard deviation = {np.std(rel):.3f}, sigma*sqrt(2*nSteps*dt) = {sigma*np.sqrt(2*nSteps*dt):.3f}, T = {dt*nSteps}")

    #plt.show()

#sigma = 1
#nSteps = 10
#dt = 1
#rel = P2(nSteps,sigma,dt)
#plotHist(rel,sigma,dt,nSteps)


L = 100
sigma = 1
nStepsList = [1000,10000,100000,1000000,10000000]
dt = 0.01
T = [x * dt for x in nStepsList]

print(nStepsList)
fig, ax = plt.subplots()
x = 0
for i in range(len(nStepsList)):
    nSteps = nStepsList[i]
    #print(T)
    rel = P2(nSteps,sigma,dt,L,N=10000)
    #print(rel)
    #fig, ax = plt.subplots()
    plt.hist(rel,histtype="step")
#plt.legend([f"{nStepsList[0]*dt}",f"{nStepsList[1]*dt}",f"{nStepsList[2]*dt}",f"{nStepsList[3]*dt}",f"{nStepsList[4]*dt}"])
plt.legend([x * dt for x in nStepsList])
plt.show()

