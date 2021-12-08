#!/usr/bin/env python3


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.style .use( 'seaborn-whitegrid' ) 



#experience
hours_a_day = [ 4,   6,   8,   16, 20 ]      #time elapsed to the projects per day (max 24 ours, min != 0)   x = hours_a_day = [0;24]
success     = [ 100, 100, 95,  50, 20 ]      # % syccessfully completed projects                             y = success = [0; 100]


k = []

for i in range( len( hours_a_day )):
    k.append( success[i] / hours_a_day[i] )

print(k)

plt.plot( k,  color='red', linestyle = 'solid', linewidth = 1, marker = "x" )
#plt.show( )

# if k >= 16,6 => syccess
# X < 4 ?????????????????   incomplete condition
#syccess >= 80%

###
w = 0.5
b = 0
###

# YES/NO logic 1/0

for i in range( len( hours_a_day )):
    X = 4
    Y = ( X * k[i] ) * w # => no syccess
    print( f"hours_a_day = {hours_a_day[i]:3};    syccess*w = {Y:20};    k = {k[i]:20};    w = 0.5" )

#Upgrade the model with the activation function:







