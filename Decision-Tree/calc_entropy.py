import os
import sys
import math
import gene_dataset
from gene_dataset import gene_dataset

def calc_entropy(dataset):
    dataset_size = len(dataset)
    label_count = {}
    for feat_vec in dataset:
        # calculate the count of each label
        cur_label =feat_vec[-1]
        label_count[cur_label] = label_count.get(cur_label, 0) + 1  

    entropy = 0.0
    for label in label_count.keys():
        prob = float(label_count[label]) / dataset_size
        entropy -= prob * math.log(prob, 2)

    return entropy

def main():
    dataset, features = gene_dataset()
    print calc_entropy(dataset)

if __name__ == "__main__":
    main()