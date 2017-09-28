# -*- coding: utf-8 -*-
import os
import sys
import math

from gene_dataset import gene_dataset
from draw_tree import createPlot
from predict import predict
from gene_tree import gene_tree

def main():
    dataset, features = gene_dataset()
    res = gene_tree(dataset, features, 0)
    print 'The output tree is: '
    print res
    print '------------------------------------------------'

    #predict the result
    test_sample = {"Occupied": "Moderate", "Price": "Cheap", "Music": "Loud", "Location": "City-Center",
        "VIP": "No", "Favorite beer": "No"}
    print 'Conditions: '
    for k, v in test_sample.items():
        print k + ": " + v,
    print ""
    print 'The prediction result is ' + predict(res, test_sample)

    createPlot(res) # draw tree by matplotlib
if __name__ == "__main__":
    main()