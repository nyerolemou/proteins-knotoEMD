#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  16 16:04:55 2020

@author: dgkounta
"""
from numpy import genfromtxt
import numpy as np
import random
from optparse import OptionParser


parser = OptionParser()   
parser.add_option("-f", "--file", help='Specify input filename.', action="store",type="string",dest="filename")
parser.add_option("-e", "--estimate", help='Estimate minimum perturbance radius',action="store_true",dest='estimate',default=False)
parser.add_option("-r", "--radius", help='Specify perturbation radius in nanometers (default = 10 nm)', action="store", type="float",dest="radius",default='10.0')
parser.add_option("-n", "--number", help='Specify number of output configurations (default = 10)', action="store", type="int",dest="numbs",default='10')
(options,args)=parser.parse_args()
optionsdict = vars(options)
inputfilename = options.filename
inputradius = options.radius
inputnumber = options.numbs
inputestimate = options.estimate


print ('Perturbing configuration.')
if inputestimate and inputradius:
    print ('NOTE: Default radius value (-r 10) will be overriden by the estimate.')


data = genfromtxt(inputfilename, delimiter=' ')

def find_min_radius(arr):
    m = np.concatenate(arr[:,None] - arr)**2
    d = np.sqrt(m[:,0]+m[:,1]+m[:,2])
    return np.min(d[d>0])

def perturb():

    xn=random.uniform(x,x+inputradius)
    yn=random.uniform(y,y+inputradius)
    zn=random.uniform(z,z+inputradius)

    r=((x-xn)**2+(y-yn)**2+(z-zn)**2)**(1/2)
    if r<inputradius:
        file1.write(str(xn)+"\t"+str(yn)+"\t"+str(zn)+"\n")
        #file1.write('(' + str(xn) + ','+ str(yn) + ','+ str(zn) +')' + ',' +"\n" )
    else:

        perturb()


if inputestimate:
    inputradius = float(find_min_radius(data))
    print ('Estimated radius: ',inputradius)

for i in range(inputnumber):
    name="%s_perturbed" %inputfilename +str(i)+".txt" 
    file = open(inputfilename, 'r')

    file1 = open(name, "w")
    for l in file:
        line = l.strip('\n').split()
    #    print(line)
        x=float(line[0])
        y=float(line[1])
        z=float(line[2])
        perturb()
    file.close()
    file1.close()

print('Done.')
