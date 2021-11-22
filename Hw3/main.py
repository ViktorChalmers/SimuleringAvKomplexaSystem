import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from Person import Person
from matplotlib import animation

def randomWalk(obj,probability,lattice):
    r = np.random.rand()
    #print(r)
    if r < probability:
        d = np.random.randint(4)
        #print(d)
        if d == 0:
            obj.move("right",lattice)
        if d == 1:
            obj.move("left",lattice)
        if d == 2:
            obj.move("up",lattice)
        if d == 3:
            obj.move("down",lattice)

def performRandomWalk(list,probability,lattice):
    for obj in list:
        randomWalk(obj,probability,lattice)

def diffusionProbability(listInfected,listSuspectible,probDiffusion):
    for objInfected in listInfected:
        r = np.random.rand()
        if r<probDiffusion:
            for objSuspectible in listSuspectible:
                if np.array_equal(objInfected.position,objSuspectible.position):
                    #print(objInfected.position, objSuspectible.position)
                    objSuspectible.updateState("infected")
                    listInfected.append(objSuspectible)
                    listSuspectible.remove(objSuspectible)


def testLists(listInfected,listSustectible,listRecovered):
    print(f"#inf = {len(listInfected)} #sus = {len(listSustectible)} #rec = {len(listRecovered)}")
    for objInfected in listInfected:
        if objInfected.state != "infected":
            print("object not infected")
    for objSuspectible in listSuspectible:
        if objSuspectible.state != "suspectible":
            print("object not suspectible")
    for objRecovered in listRecovered:
        if objRecovered.state != "recovered":
            print("object not recovered")

    xInfected = [obj.position[0] for obj in listInfected]
    yInfected = [obj.position[1] for obj in listInfected]

    xSuspectible = [obj.position[0] for obj in listSuspectible]
    ySuspectible = [obj.position[1] for obj in listSuspectible]

    xRecovered = [obj.position[0] for obj in listRecovered]
    yRecovered = [obj.position[1] for obj in listRecovered]
    #print(position)
    plt.plot(xInfected,yInfected,"o",color="red")
    plt.plot(xSuspectible,ySuspectible,"*",color="blue")
    plt.plot(xRecovered,yRecovered,"p",color="green")
    plt.show()

def recoverProbability(listInfected,probRecover):
    for objInfected in listInfected:
        gamma = np.random.rand()
        if gamma < probRecover:
            objInfected.updateState("recovered")
            listRecovered.append(objInfected)
            listInfected.remove(objInfected)


def runSIR(listInfected,listSuspectible,listRecovered):
    #testLists(listInfected,listSuspectible,listRecovered)
    performRandomWalk(listSuspectible,probRandomWalk,lattice)
    performRandomWalk(listInfected,probRandomWalk,lattice)
    performRandomWalk(listRecovered, probRandomWalk,lattice)
    diffusionProbability(listInfected,listSuspectible,probDiffusion)
    recoverProbability(listInfected,probRecover)

lattice = 100
nSuspectible = 990
nInfected = 10
nRecovered = 0
listSuspectible = [Person(state = "suspectible", lattice = lattice) for i in range(nSuspectible)]
listInfected = [Person(state = "infected", lattice = lattice) for i in range(nInfected)]
listRecovered = [Person(state = "infected", lattice = lattice) for i in range(nRecovered)]
#print(len(listRecovered))

probRandomWalk = 0.8
probDiffusion = 0.6
probRecover = 0.01


for obj in listSuspectible:
    randomWalk(obj,probRandomWalk,lattice)

for obj in listInfected:
    randomWalk(obj,probRandomWalk,lattice)


#testLists(listInfected,listSuspectible,listRecovered)
timeStep = 0
nrInfected = []
nrSuspectible = []
nrRecovered = []
while len(listInfected):
    runSIR(listInfected,listSuspectible,listRecovered)
    nrInfected.append(len(listInfected))
    nrSuspectible.append(len(listSuspectible))
    nrRecovered.append(len(listRecovered))
    if timeStep % 10 == 0:
        print(f"timestep = {timeStep} #inf = {len(listInfected)} #sus = {len(listSuspectible)} #rec = {len(listRecovered)}")
    timeStep += 1

print(timeStep)
plt.plot(nrInfected,color="orange")
plt.plot(nrSuspectible,color="blue")
plt.plot(nrRecovered,color="green")
plt.show()
testLists(listInfected,listSuspectible,listRecovered)



