#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt
from scipy import linalg

def linear_regression(dataset):
    point_data = np.array(dataset[:, :2])
    m, n = point_data.shape
    label = np.array([dataset[:, 2]])
    print label.shape
    point_data = np.c_[np.ones((m, 1)), point_data]
    theta = np.dot(np.dot(linalg.inv(np.dot(point_data.T, point_data)), \
        point_data.T), label.T)
    print "Result"
    print theta

def main():
    data = np.loadtxt("linear-regression.txt",delimiter=",")
    linear_regression(data)

if __name__ == "__main__":
    main()