import numpy as np
import os
import sys
from scipy import linalg

k = 3
eps =  0.000001
max_itertime = 1000

def fit_EM(X):        
    # n = number of data-points, d = dimension of data points        
    n, d = X.shape
    
    # randomly choose the starting centroids/means 
    ## as 3 of the points from datasets        
    mu = X[np.random.choice(n, k, False), :]
    #from range(n) choose k points without replacement
    
    # initialize the covariance matrices for each gaussians
    Sigma= [np.eye(d)] * k
    
    # initialize the probabilities/weights for each gaussians
    w = [1./ k] * k
    
    # responsibility matrix is initialized to all zeros
    # we have responsibility for each of n points for eack of k gaussians
    R = np.zeros((n, k))
    
    ### log_likelihoods
    log_likelihoods = []
    P = lambda mu, s: np.linalg.det(s) ** -.5 ** (2 * np.pi) ** (-X.shape[1]/2.) \
            * np.exp(-.5 * np.einsum('ij, ij -> i',\
                    X - mu, np.dot(np.linalg.inv(s) , (X - mu).T).T ) ) 
                    
    # Iterate till max_iters iterations        
    while len(log_likelihoods) < max_itertime:
        
        # E - Step
        
        ## Vectorized implementation of e-step equation to calculate the 
        ## membership for each of k -gaussians
        for i in range(k):
            R[:, i] = w[i] * P(mu[i], Sigma[i])

        ### Likelihood computation
        log_likelihood = np.sum(np.log(np.sum(R, axis = 1)))
        
        log_likelihoods.append(log_likelihood)
        
        ## Normalize so that the responsibility matrix is row stochastic
        R = (R.T / np.sum(R, axis = 1)).T
        
        ## The number of datapoints belonging to each gaussian            
        N_ks = np.sum(R, axis = 0)
        
        
        # M Step
        ## calculate the new mean and covariance for each gaussian by 
        ## utilizing the new responsibilities
        for i in range(k):
            
            ## means
            mu[i] = 1. / N_ks[i] * np.sum(R[:, i] * X.T, axis = 1).T
            x_mu = np.matrix(X - mu[i])
            
            ## covariances
            Sigma[i] = np.array(1 / N_ks[i] * np.dot(np.multiply(x_mu.T,  R[:, i]), x_mu))
            
            ## and finally the probabilities
            w[i] = 1. / n * N_ks[i]
        # check for convergence
        if len(log_likelihoods) < 2 : continue
        if np.abs(log_likelihood - log_likelihoods[-2]) < eps: break

    print "=============Mean============"
    print mu
    print "===========Amplitude========="
    print w
    print "======Covariance Matrix======"
    print Sigma

def main():
    data = np.loadtxt("clusters.txt",delimiter=",")
    # data = np.loadtxt("test.txt", delimiter=",")
    fit_EM(data)
if __name__ == "__main__":
    main()