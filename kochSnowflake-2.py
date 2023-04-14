"""
Math 96F
Koch Snowflake
"""

import numpy as np
import matplotlib.pyplot as plt

import fourPoint

from numpy import pi, cos, sin

# Equilateral triangle
theta = np.linspace( pi/2, 5*pi/2, 4)
x, y = cos(theta), sin(theta)

vertices = np.array([x,y])

# Applying modification to the first side

newvertices = np.zeros((2,10))

newvertices[:,:4] = fourPoint.generate(vertices[:,0], vertices[:,1])

newvertices[:,4:8] = fourPoint.generate(vertices[:,1], vertices[:,2])

newvertices[:,8:] = vertices[:,2:]

# Plotting
fig, ax = plt.subplots()
ax.set_aspect('equal')

ax.plot( newvertices[0,:], newvertices[1,:])
ax.scatter( newvertices[0,:], newvertices[1,:], c='k')

# P = np.array([x[0], y[0]])
# Q = np.array([x[1], y[1]])

# A = (2*P + Q)/3
# C = (P + 2*Q)/3

# x = [ x[0] , A[0], C[0], x[1], x[2], x[3] ] 
# y = [ y[0] , A[1], C[1], y[1], y[2], y[3] ] 

# ax.clear()
# ax.plot( x, y)
# ax.scatter( x, y, c='k')