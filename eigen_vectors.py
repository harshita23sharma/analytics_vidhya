 # Eigenvectors is the backbone of PCA

 # multiply a 2-dimensional vector with a 2*2 matrix .This operation on a vector is called linear transformation.
 #  Note that on applying a linear transformation to yellow coloured vector, its direction changes but the direction of the red coloured vector doesn’t change even after applying the linear transformation. The vector coloured in red is an example of Eigenvector.
 #  Precisely, for a particular matrix; vectors whose direction remains unchanged even after applying linear transformation with the matrix are called Eigenvectors for that particular matrix. 
#  Ax = cx

# (A-c)x = 0  …….(1)

# Please note that in the term (A-c), ‘c’ denotes an identity matrix of the order equal to ‘A’ multiplied by a scalar ‘c’

import  numpy as np

#create an array
arr = np.arange(1,10).reshape(3,3)

#finding the Eigenvalue and Eigenvectors of arr
np.linalg.eig(arr)