#!/usr/bin/env python3
"""
@author: nyerolemou
"""
import numpy as np
from pyemd import emd

F_DISTANCE_PATH = "../data/f_distance_matrix.txt"

def load_f_distmat():
    '''
    Load the distance matrix of knotoid f-distances, setting default to 
    unknown knotoid types (crossing number >6) to 2.
    '''
    path = F_DISTANCE_PATH
    fdistmatcomp = np.loadtxt(path, skiprows=1, usecols=np.arange(1,643))
    row = np.ones((1,642))*2
    col = np.ones((642,1))*2
    col1 = np.vstack([col,np.zeros((1,1))])
    fdistmatcomp = np.vstack([fdistmatcomp,row])
    fdistmatcomp = np.hstack([fdistmatcomp,col1])
    return fdistmatcomp

def knotoid_types():
    '''
    Load all knotoid types up to crossing number 6, plus unknown. This is the order
    in which the distribution bins are maintained.
    '''
    path = F_DISTANCE_PATH
    knotoidKeysComp = np.loadtxt(path, dtype=str, max_rows=1, usecols=np.arange(0,642))
    knotoidKeysComp = np.hstack([knotoidKeysComp,np.array(['UNKNOWN'])])
    return knotoidKeysComp 


if __name__ == "__main__":
	cost_matrix = load_f_distmat()

	# generate some random distributions with integer entries summing to 5000
	toy_data1 = np.random.randint(5, size=642)
	toy_data2 = np.random.randint(3, size=642)
	knotoid_distribution1 = np.hstack([5000-np.sum(toy_data1), toy_data1])
	knotoid_distribution2 = np.hstack([5000-np.sum(toy_data2), toy_data2])

	distance = emd(knotoid_distribution1/5000, knotoid_distribution2/5000, cost_matrix)

	print(distance)