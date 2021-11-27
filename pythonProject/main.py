import numpy as np
import matplotlib.pyplot as plt



def P1(N,n,m,T,R,P,S):

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

if __name__ == '__main__':
    N = 10
    T = 0
    R = 0.5
    P = 1
    S = 1.5
    summ = np.zeros(N)
    m=6
    summ = np.zeros([N,N])
    for m in range(N):
        for n in range(N):
            summ[n,m] = P1(N,n,m,T,R,P,S)
    #plt.plot(summ,"o")
    #plt.axvline(x=m)
    #plt.show()
    print(summ)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
