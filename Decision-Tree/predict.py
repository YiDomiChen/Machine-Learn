import os
import sys
import math

from gene_dataset import gene_dataset
from gene_tree import gene_tree

def predict(tree, test_sample):
    if type(tree).__name__=='str':
        return tree
    else:
        sel_feature = tree.keys()[0]
        return predict(tree[sel_feature][test_sample[sel_feature]], test_sample)