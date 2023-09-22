import numpy as np
from sympy import *
from parameters import *

def augmented_rref(var1, var2, var3, var4):
    matrix = np.zeros((4,4))
    matrix[:, 0] = var1
    matrix[:, 1] = var2
    matrix[:, 2] = var3
    matrix[:, 3] = var4
    
    p, q, r, s = symbols('p q r s')
    column = np.array([[-p], 
                      [-q],
                      [-r],
                      [-s]])
    augmented_matrix = Matrix(np.hstack((matrix, column)))
    rref = augmented_matrix.rref()
    return rref

def dimensionless(dimensions, matrix):
    p, q, r, s = symbols('p q r s')
    equations = matrix[0][:, -1]
    vector = equations.subs({p:dimensions[0], q:dimensions[1], r:dimensions[2], s:dimensions[3]})
    return vector

