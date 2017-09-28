import os
import sys
import math
from collections import Counter

import calc_entropy
import gene_dataset
import get_max_infogain_feat

from gene_dataset import gene_dataset
from gene_dataset import get_featval
from calc_entropy import calc_entropy
from get_max_infogain_feat import get_max_infogain_feat

def gene_tree(dataset, propset, level):
    # configure nodes
    class_vec = [v[-1] for v in dataset]
    if len(set(class_vec)) == 1: # terminate criteria 1: all samples have the same label
        return class_vec[0]

    if not propset: # terminate criteria 2: running out of features
        class_counter = Counter(class_vec)
        pair = class_counter.most_common()
        count = -1
        for i in range(len(set(class_counter.elements()))):
            if count == -1:
                count = pair[i][1]
            else:
                if pair[i][1] != count:
                    return class_counter.most_common(1)[0][0]
        
        return 'tie'    # if the count of each number is equal, return a tie
    best_feat_idx, max_infogain = get_max_infogain_feat(dataset)   

    #featval_list = [v[best_feat_idx] for v in dataset]
    #featval_set = set(featval_list)
    feat_map = get_featval()
    feat_valset = feat_map[propset[best_feat_idx]]
    #print level
    #print feat_valset

    tree_dict = {propset[best_feat_idx]:{}}
    for k in feat_valset:
    #for val in featval_set:    
        #print best_feat_idx
        #print feat_valset[k]
        subdataset = [v for v in dataset if v[best_feat_idx] == feat_valset[k]]
        #subdataset = [v for v in dataset if v[best_feat_idx] == val]
        subdataset = split_dataset(subdataset, best_feat_idx)

        subpropset = propset[:] # deep copy
        del(subpropset[best_feat_idx])
        if len(subdataset) > 0:    
            tree_dict[propset[best_feat_idx]][k] = gene_tree(subdataset, subpropset, level + 1)
            #print tree_dict[propset[best_feat_idx]][k]
            #tree_dict[propset[best_feat_idx]][val] = gene_tree(subdataset, subpropset, level + 1)
        else:
            tree_dict[propset[best_feat_idx]][k] = "tie"

    return tree_dict

def split_dataset(dataset, col_idx):
    subset = []
    for feat_vec in dataset:
        subvec = feat_vec[:col_idx]
        subvec.extend(feat_vec[col_idx + 1:])
        subset.append(subvec)

    return subset

def main():
    dataset, features = gene_dataset()
    res = gene_tree(dataset, features, 0)
    print '---------final result-----------'
    print res

if __name__ == "__main__":
    main()