#print(np.load("R(beta,gamma=0,01).npy"))
#print(np.load("R(beta,gamma=0,02).npy"))
#avg = 2
#beta = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
#R = np.zeros(len(beta))
#gammalist = [0.01,0.02]
#for j in range(len(gammalist)):
    #R = np.zeros(len(beta))
    #gamma = gammalist[j]
   # for i in range(len(beta)):
  #      probDiffusion = beta[i]
 #       for k in range(avg):
#            R[i] +=  P1(lattice=100,
              #              nSuspectible=990,
             #               nInfected=10,
            #                nRecovered=0,
           #                 nDead=0,
          #                  probRandomWalk=0.8,
         #                   probDiffusion = probDiffusion,
        #                    probRecover=gamma,
       #                     probDeath = 0,
      #                      probSusceptible = 0,
     #                       plott=False
    #                        )/avg
   #     print(f"----------------------------------gamma={gammalist[j]}, R={R[i]}, beta={beta[i]}")
  #  plt.plot(beta,R,"o")
 #   np.save(f"R(beta,gamma={gamma})".replace(".",","), R)


#plt.title("Final number of recovered agends as a function of the infection rate")
#plt.legend(gammalist)

#plt.savefig(f"AverageR_over_multiple_Beta2".replace(".",","))
#plt.show()

beta = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
gamma = [0.01,0.02]
R1 = [45,330,650,760,840,850,860,840,850,860]
R2 = [45,50,110,200,390,500,600,630,690,700]
#print(len(R2),len(beta))
#plt.plot(beta,R1,"o")
#plt.plot(beta,R2,"o")
Z = np.array([R1])
X = np.array(beta)
Y = np.array(gamma)
RRR = [R1,R2]
#print(X)
#print(Y)
#print(Z)
#print([X,Y])

beta_gamma0 = X/Y[0]
beta_gamma1 = X/Y[1]
bg = np.linspace(5,50,10)
bg = np.concatenate((bg, np.linspace(60,100,5)))
#0.1,.01 & 0.2,0.02
#print(beta_gamma0)
#print(beta_gamma1)
print(X)
print(bg)
i = 0
j = 0
print(X[i]/gamma[j])
RR=np.zeros([10,10])

RR[0,0] = 0
RR[0,1] = RRR[1][0]

RR[1,0] = RRR[0][0]
RR[1,1] = RRR[1][1]

RR[2,0] = 0
RR[2,1] = 0

RR[3,0] = 0
RR[3,1] = 0

RR[4,0] = 0
RR[4,1] = 0

RR[5,0] = 0
RR[5,1] = 0

RR[6,0] = 0
RR[6,1] = 0

RR[7,0] = 0
RR[7,1] = 0

print(RR)

plt.contourf(X,bg,RR)
plt.show()