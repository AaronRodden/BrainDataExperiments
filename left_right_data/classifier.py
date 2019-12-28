import pandas as pd
import numpy as np
import scipy.io as sio
import os

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier, Perceptron
from feats_from_mat import get_feats_from_mat 

def data_splits():
    print("Collecting features...")
    train_data = get_feats_from_mat("data\\train")
    return train_data


# so if this works all I need to do is combine these two dicst...
def getXY(feat_list):
#    X = [ feat[1] for feat in feat_list ]
#    Y = [ feat[0] for feat in feat_list ]
#    
    X = feat_list["eeg"]
    Y = feat_list["direction"]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.0)
    return X,Y

if __name__ == "__main__":
    pass
    train = data_splits()
    X, Y = getXY(train)
#    print(X)
#    print(Y)
#    X, y = load_iris(return_X_y=True)
#    print(X)
#    print(y)
    clf = LogisticRegression(random_state=0)
#    clf = SGDClassifier(loss = "log", verbose = True)
    print("Training model...")
    clf.fit(list(X),Y)
    print(clf.predict(X[:2, :]))
    print(clf.score(X,Y))
#    print(X)
#    print(len(X))
#    print(Y)
#    print(len(Y))

