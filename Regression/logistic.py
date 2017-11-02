#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt
from scipy import linalg


def logistic_regression(dataset):
    cur_iter, max_iter = 0, 7000
    # test_arr = np.ones((5,5))
    # g = sigmoid(test_arr)
    point_data = dataset[:, :3]
    m, n = point_data.shape
    point_data = np.c_[np.ones((m, 1)), point_data] #(m, n + 1)
    label = np.array([dataset[:, 4]])   #(m, 1)
    theta = np.ones((n + 1, 1))

    alpha = 0.001
    while cur_iter < max_iter:
        # cost_function(point_data, theta, label)
        h = hypothesis(point_data, label, theta)
        derivative = -1. / m * np.dot(point_data.T, h * label.T)
        theta = theta - alpha * derivative

        cur_iter += 1

    print 'Final Result'
    print theta 

    h = hypothesis(point_data, label, theta)
    count = 0
    for i in range(m):
        # print h[i, 0]
        if h[i, 0] > 0.5:
            if label[0, i] == 1:
                count += 1
        elif h[i, 0] < 0.5:
            if label[0, i] == -1:
                count += 1

    print count * 1. / 2000


# def cost_function(dataset, theta, label):
#     m, n = dataset.shape
#     h = hypothesis(dataset, theta)
#     prediction = - 1. / m * (np.multiply((np.log(h)).T, label) + np.multiply(np.log(1 - h).T, (1 - label)))

#     return prediction

def hypothesis(dataset, label, theta):
    m, n = dataset.shape
    z = label.T * np.dot(dataset, theta)
    # print z.shape   # (m * 1)
    g = 1. / (1 + np.exp(z))
    # print g.shape   # (m * 1)
    return g


def main():
    data = np.loadtxt("classification.txt",delimiter=",")
    logistic_regression(data)

if __name__ == "__main__":
    main()