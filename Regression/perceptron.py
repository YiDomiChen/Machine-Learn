#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt
from scipy import linalg


def perceptron(dataset):
    point_data = dataset[:, :3]
    m, n = point_data.shape
    point_data = np.c_[np.ones((m, 1)), point_data] # (m, n + 1)
    label = np.array([dataset[:, 3]])   #(m, 1)
    theta = np.ones((n + 1, 1))
    h = np.dot(point_data, theta)   
    h[h < 0] = -1
    h[h > 0] = 1
    alpha = 0.5
    while ((h == label).all()):
        for i in range(m):
            if h[m, 0] != label[m, 0]:
                if label[m, 0] == 1:
                    theta = theta + alpha * point_data[m, :].T
                elif label[m, 0] == -1:
                    theta = theta - alpha * point_data[m, :].T
    print 'tt'

def main():
    data = np.loadtxt("classification.txt",delimiter=",")
    perceptron(data)

if __name__ == "__main__":
    main()