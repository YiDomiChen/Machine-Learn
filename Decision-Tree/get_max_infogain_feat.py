import os
import sys
import math

import calc_entropy
import gene_dataset
from gene_dataset import gene_dataset
from calc_entropy import calc_entropy

def get_max_infogain_feat(dataset):
    """Get the feature with maximum information gain
    
    Args:
        dataset: The input dataset with labels
    
    Returns:
        A tuple containing the feature index and the value of its 
        corresponding information gain.
    """
    base_entropy = calc_entropy(dataset)
    feat_count = len(dataset[0]) - 1
    max_infogain = 0.0
    best_feat_index = 0 # if there is no infogain, try to select the feature with order priority as the optimal feature
    for i in range(feat_count): 
        featval_list = [sample[i] for sample in dataset]
        feat_set = set(featval_list)
        subset_infogain = 0.0
        subset_entropy = 0.0    
        for val in feat_set:
            subdataset = [sample for sample in dataset if sample[i] == val]
            subset_weight = float(len(subdataset)) / float(len(dataset))
            subset_entropy += subset_weight * calc_entropy(subdataset)
        subset_infogain = base_entropy - subset_entropy
        if subset_infogain > max_infogain:
            max_infogain = subset_infogain
            best_feat_index = i



    return best_feat_index, max_infogain
        
def main():
    dataset, features = gene_dataset()
    get_max_infogain_feat(dataset)

if __name__ == "__main__":
    main()