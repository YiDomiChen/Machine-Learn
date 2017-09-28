from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np
import graphviz

from gene_dataset import gene_dataset

def generate():
    # clf = tree.DecisionTreeClassifier()
    # dataset, features = gene_dataset()
    # dataset = np.array(dataset)
    # clf = clf.fit(dataset[:,:-1],dataset[:,-1:])
    # dot_data = tree.export_graphviz(clf, out_file=None) 
    # graph = graphviz.Source(dot_data)
    # graph.render("ggg")
    # dot_data = tree.export_graphviz(clf, out_file=None, 
    #                      feature_names=features,  
    #                      class_names=np.array(['Y', 'N']),  
    #                      filled=True, rounded=True,  
    #                      special_characters=True)
    # graph = graphviz.Source(dot_data)
    # graph
    clf = tree.DecisionTreeClassifier()
    dataset, features = gene_dataset()
    dataset = np.array(dataset)
    clf = clf.fit(dataset[:,:-1],dataset[:,-1:])
    dot_data = tree.export_graphviz(clf, out_file=None) 
    graph = graphviz.Source(dot_data)
    graph.render("iris")
    dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=np.array(['Y', 'N']),  
                         filled=True, rounded=True,  
                         special_characters=True)
    graph = graphviz.Source(dot_data)
    graph


def main():
    generate()

if __name__ == "__main__":
    main()