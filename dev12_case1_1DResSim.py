#Pressure
import numpy as np 
#Reservoir properties
por = 0.3
visc = 0.7
Cr = 0.000008
perm = 60
dx = 250.0
dy = 250.0
lx = 5000.0
ly = 5000.0

#initial conditions
pres = 1000.0
pleft = 1000.0
ptop = 1000.0
pright = 500.0
pbottome = 500.0

#timestep
ts = 1.0 #hours
tc = 100.0

#Number of grids
nx = lx/dx
ny = ly/dy
ncels = nx * ny

#dimensionless vars
betha = por*visc*Cr/(0.0002637 * perm)
alpha = ((dx**2)*(dy**2)*betha) / ts
sigma = (2*(dy**2)) + (2 * (dx**2)) + alpha

#matrix
matA = np.eye(int(nx))* -betha

inv_matA = np.zeros(int(ncels)).reshape(int(nx),int(ny))


#RHS
#matP
print(matA)




