#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Implimentation of FastMap Algorithm
Plot the Damerau Levenshtein distances of words based on the resulat of fastmap

Author: Yi Chen
Created Date: Oct. 12, 2017
'''
import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt
from scipy import linalg


eps = 0.0001
def fastmap(dataset):
    np.set_printoptions(suppress=True)
    max_iter = 3
    iter_time = 0
    maxobj_id = int(max(dataset[:, 1]))
    dim_arr = np.zeros((max_iter, maxobj_id))
    while iter_time < max_iter:
        print "iter time, " + str(iter_time)
        print "======dis matrix======="
        print dataset      
        ds_list = dataset.tolist()
        maxdist = -sys.maxint
        a_idx, b_idx = -1, -1
        for n in range(len(dataset)):
            if dataset[n, 2] > maxdist:
                maxdist = dataset[n, 2]
                a_idx, b_idx = dataset[n, 0], dataset[n, 1]

        print "======pivot========"
        print a_idx, b_idx
        

        x_arr = np.zeros((1, maxobj_id))
        for i in range(1, maxobj_id + 1):
            dai, dbi = 0, 0
            da_arr = [r for r in ds_list if int(r[0]) == i and int(r[1]) == a_idx or int(r[0]) == a_idx and int(r[1]) == i]
            if len(da_arr) > 0:
                dai = da_arr[0][2]
            db_arr = [r for r in ds_list if int(r[0]) == i and int(r[1]) == b_idx or int(r[0]) == b_idx and int(r[1]) == i]
            if len(db_arr) > 0:
                dbi = db_arr[0][2]
            xi = (dai ** 2 + maxdist ** 2 - dbi ** 2) / (2 * maxdist)
            x_arr[0, i - 1] = xi
        print "======axis========"
        print x_arr

        for n in range(len(dataset)):
            i, j = int(dataset[n, 0]), int(dataset[n, 1])
            xi, xj = x_arr[0, i - 1], x_arr[0, j - 1]
            if dataset[n, 2] ** 2 - (xi - xj) ** 2 < 0:
                print "(xi - xj) ^ 2 = "  + str((xi - xj) ** 2) + " ---- O(i,j) ^ 2 " + str(dataset[n, 2] ** 2)
            dataset[n, 2] = np.sqrt(dataset[n, 2] ** 2 - (xi - xj) ** 2)
        dim_arr[iter_time] = x_arr

        iter_time += 1

    return dim_arr

def plot_words(coords, words):
    plt.title('Distance Plot of Given Words')
    plt.scatter(coords[0, :], coords[1, :])
    for i in range(len(words)):
        plt.annotate(words[i], xy = (coords[0, i], coords[1, i]))
    plt.show()

def main():
    data = np.loadtxt("fastmap-data.txt",delimiter="\t")
    coords = fastmap(data)
    words = []
    with open('fastmap-wordlist.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    print words
    plot_words(coords, words)

if __name__ == "__main__":
    main()