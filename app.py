#!/usr/bin/env python3


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.style .use( 'seaborn-whitegrid' ) 



#experience
#hours_a_day = [ 0,   4,   6,   8,   16, 20, 24 ]      #time elapsed to the projects per day (max 24 ours, min != 0)   x = hours_a_day = [0;24]
#success     = [ 0,   100, 100, 95,  50, 20, 0  ]      # % syccessfully completed projects                             y = success = [0; 100]
hours_a_day = [ 4,   6,   8,   16, 20 ]      #time elapsed to the projects per day (max 24 ours, min != 0)   x = hours_a_day = [0;24]
success     = [ 100, 100, 95,  50, 20 ]      # % syccessfully completed projects                             y = success = [0; 100]

#plt.plot( hours_a_day, success, color='green', linestyle = 'solid', linewidth = 1, marker = "x" )
#plt.show( )

## --------------------------------------------------------------------------------------###
# График похож на параболу. Парабола - график квадратичной функции: y = a*x^2 + b*x + c
# Ветви параболи направленны вниз, значит a < 0
# При x = 0 => y = 0, значит с = 0
# Получается: y = -a*x^2 + b*x
# Корни уравнения: y = 0 при x = 0.001
# 0 = -a*576 +24*b => b = 24a => y = a*x*( x + 24 )
# a = y/( x^2 + 24*x )
## --------------------------------------------------------------------------------------###

#a = []

#for i in range( len( hours_a_day )):
#    a.append( success[i] / (hours_a_day[i] * hours_a_day[i] + 24 * hours_a_day[i] )) #error: Divizion by zero

#print(a)

#plt.plot( a,  color='red', linestyle = 'solid', linewidth = 1, marker = "x" )
#plt.show( )

w = np.random.normal()
#rint(w)

def sigmoid(x):
    return 1 / (1 + np.exp( -1 ))

class Neuron:
    
    def __init__( self, weight ):
        self.weight = weight
    
    def feedForward( self, inputs ):
        total = np.dot( self.weight, inputs )
        return sigmoid( total )

n = Neuron( w )
print(n.feedForward( hours_a_day ))



