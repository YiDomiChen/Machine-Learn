import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt
from scipy import linalg

k = 3
eps =  0.000001
max_itertime = 1000

def gmm(dataset):

    # np.random.seed(100)
    n, d = dataset.shape
    print dataset[:,0]
    mu = dataset[np.random.choice(n, k, False), :]
    # mu = np.zeros((k, d))
    # mu[0] = dataset[5]
    # mu[1] = dataset[21]
    # mu[2] = dataset[26]

    sigma = np.zeros((k, d, d))
    for i in range(k):
        sigma[i] = np.eye(d, d) * 0.1
    A = [1. / k] * k
    PM = np.zeros((n, k))


    last_likelihood = -1
    iter_time = 0

    while True:
        for i in range(k):
            x_mu = np.array(dataset - mu[i])
            # print x_mu.T.shape
            for j in range(n):
                # PM[j, i] = A[i] * linalg.det(sigma[i]) ** -.5 ** (2 * np.pi) ** (-d / 2) * np.exp(-0.5 * np.dot(np.dot(x_mu[j], linalg.inv(sigma[i])), x_mu[j].T)) 
                # Estimation Step
                PM[j, i] = A[i] / (linalg.det(sigma[i]) ** 0.5 * (2 * np.pi) ** (-d / 2)) * np.exp(-0.5 * np.dot(np.dot(x_mu[j], linalg.inv(sigma[i])), x_mu[j].T)) 
                
        tmp = np.array([np.sum(PM, axis = 1)])
        PM = PM / tmp.T
        
        # Maximum Step
        for i in range(k):
            mu[i] = np.sum(PM[:, i] * dataset.T, axis = 1) / np.sum(PM[:, i], axis = 0)
            # print mu[i].shape
            x_mu = np.array(dataset - mu[i])
            sigma[i] = 1. / np.sum(PM[:, i], axis = 0) * np.dot(np.multiply(PM[:, i], x_mu.T), x_mu)
            A[i] = 1. * np.sum(PM[:, i], axis = 0) / n

        # likelyhood = np.sum(np.log(tmp))
        likelihood = np.sum(np.log(np.sum(PM, axis = 1)))
        if iter_time < 2:
            iter_time = iter_time + 1
            continue
        if np.abs(last_likelihood - likelihood) < eps:
            print 'iteration break condition: likelihood difference less than epsilon'
            break
        if iter_time >= max_itertime:
            print 'iteration break condition: exceed max iteration times'
            break
        last_likelihood = likelihood
        iter_time += 1


    print "=============Mean============"
    print mu
    print "===========Amplitude========="
    print A
    print "======Covariance Matrix======"
    print sigma


    l = np.argmax(PM, axis = 1) # select the cluster with the maximum gamar 
    # print l

    #plot the result
    plt.scatter(dataset[:, 0], dataset[:, 1], c=l)
    plt.title('Clustering result of GMM')
    plt.xlim(dataset[:, 0].min() * 1.1, dataset[:, 0].max() * 1.1)
    plt.ylim(dataset[:, 1].min() * 1.1, dataset[:, 1].max() * 1.1)

    ind_x = math.ceil(dataset[:, 0].max()) - math.floor(dataset[:, 0].min()) + 1
    x_ticks = np.linspace(math.floor(dataset[:, 0].min()), math.ceil(dataset[:, 0].max()), ind_x)
    plt.xticks(x_ticks)
    ind_y = math.ceil(dataset[:, 1].max()) - math.floor(dataset[:, 1].min()) + 1
    y_ticks = np.linspace(math.floor(dataset[:, 1].min()), math.ceil(dataset[:, 1].max()), ind_y)
    plt.yticks(y_ticks)

    ax = plt.gca()
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))    

    plt.show()


def main():
    data = np.loadtxt("clusters.txt",delimiter=",")
    # data = np.loadtxt("test.txt", delimiter=",")
    gmm(data)
    
if __name__ == "__main__":
    main()
