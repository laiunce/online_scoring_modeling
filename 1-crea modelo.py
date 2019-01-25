#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 03:39:20 2018

@author: laiunce
"""

from sklearn import svm
from sklearn import datasets
import pickle


clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)  

# now you can save it to a file
with open('/Users/laiunce/projects/api/modelo_api/2-modelo.pkl', 'wb') as f:
    pickle.dump(clf, f)
