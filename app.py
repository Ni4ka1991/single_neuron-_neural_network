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


###
w = 0.5
b = 0
###

#1
X = 4
Y = ( X * k[0] ) * w # => yes syccess

#2
X = 6
Y = ( X * k[1] ) * w # => yes syccess

#3
X = 8
Y = ( X * k[2] ) * w # => no syccess

#4
X = 16
Y = ( X * k[3] ) * w # => no syccess

#5
X = 20
Y = ( X * k[4] ) * w # => no syccess

