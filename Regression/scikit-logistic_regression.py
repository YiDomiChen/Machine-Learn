from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np


def loadDataSet():
	data=np.loadtxt("classification.txt",delimiter=",")
	X=np.ones((data.shape[0],4))
	X[:,1:]=data[:,0:3] #input values Xj for each example j
	D=data[:,4] #desired output Dj
	return X,D

def main():
	X,D=loadDataSet()
	clf=LogisticRegression()
	clf.fit(X,D)
	print "Weights are:",clf.coef_
	scores = cross_val_score(clf, X, D, cv=5)
	print "Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)

if __name__ == "__main__":
    main()
