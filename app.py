#!/usr/bin/env python3


import numpy as np
from os import system
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.style .use( 'seaborn-whitegrid' ) 



#DATA
hours_a_day = [ 4,   6,   8,  12,  16, 20, 22 ]      #time elapsed to the projects per day (max 24 ours, min != 0)   x = hours_a_day = [0;24]
success     = [ 100, 100, 95, 75,  50, 20, 0  ]      # % syccessfully completed projects                             y = success = [0; 100]

#plt.plot( hours_a_day, success, color = "green", linestyle="solid", linewidth = 1, marker = "x")
#plt.show()

#syccess >= 80%
Y_N_success = []

def success_func( var, succ_persent ):
 for i in range( len( var )):
     i = True if var[i] >= succ_persent else False
     Y_N_success.append(i)

success_func( success, 80 )
###


#Approximate dependence
k = []

for i in range( len( hours_a_day )):
    k.append( success[i] / hours_a_day[i] )
###


#NEURON

w = 0.5
b = 0
###

def sigmoida(var):
    return 1 / ( 1 + np.exp(- var ))

#Upgrade the model with the activation function:
system( "clear" )
w = 0.5
for u in range(80):
    print()
    print( f"######## EPOCH {u} #######" )
#    print(w)
    for i in range( len( hours_a_day )):
        X = 4
        Y = ( X * k[i] ) * w
        S = sigmoida(Y)
        yes = True if S >= 0.99 else False
        err = False
        if( yes != Y_N_success[i] ):
            err = True
            r = np.random.normal()
#            print(r)
            w += r
        print( f"Calculated success f(w)= {yes:3};  Test data = {Y_N_success[i]:3};  Correct/Incorrect resolved = {err}" )








# if k >= 16,6 => syccess
# X < 4 ?????????????????   incomplete condition
