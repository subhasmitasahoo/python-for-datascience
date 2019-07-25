# Linear Algebra Library for Python
# pip install numpy 
# conda install numpy

# NumPy Arrays
#.................................................................
# 1. vectors (1D), 2. Matrices

import numpy as np

my_list = [1,2,3]

arr = np.array(my_list)
print(arr)


my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))

# for quickly generating arrays
print(np.arange(0,10))
print(np.arange(0,11,2)) # Third argument is step size

print(np.zeros((5,10)))

print(np.ones(10))

print(np.linspace(0, 10, 5)) #Returns 5 evenly spaced points

#Identity Matrix
print(np.eye(5))

#Random Matrix
print(np.random.rand(5, 10))

#Normal Distribution
print(np.random.randn(5, 10))

print(np.random.randint(1, 100, 10))

#Reshape method
arr = np.arange(25)
arr = arr.reshape(5,5)
print(arr)

#Max Min Method
print(arr.max())
print(arr.argmax()) #returns the index of max value
print(arr.shape)
print(arr.dtype)

