#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt
from scipy import linalg


def con(dataset):
    # a = 2 * np.ones(5)
    # print a.shape
    # print dataset.shape
    # b = np.c_[a, dataset.T]

    # print b
    # a=np.array([[1,1],[0,1]])
    a = np.ones((5, 2))
    b = np.ones((5, 2))
    b[1,0] = 2
    b[1,1] = 2
    b[3,1] = 4
    
    c = a == b
    print np.nonzero(c)
    # b=np.arange(4).reshape((2,2))
    # print a + b

def main():
    data = np.loadtxt("classification.txt",delimiter=",")
    con(data)

if __name__ == "__main__":
    main()

