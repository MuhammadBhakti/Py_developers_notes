#Matrix notes
import numpy as np 

""" 
Membuat matrix pada python dengan berbagai macam cara

"""
#1
mat_a = np.matrix('1,2; 3,4')
print(mat_a)
#2
mat_a = np.matrix([[1,2],[3,4]])
print(mat_a)
#3
mat_a = np.zeros(25).reshape(5,5)
print(mat_a)
#4
mat_a = np.ones(25).reshape(5,5)
print(mat_a)
#5
mat_a = np.arange(25).reshape(5,5)
print(mat_a)
#6
mat_a = np.linspace(1,10,num=25).reshape(5,5)
print(mat_a)

