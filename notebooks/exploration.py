# %%
import numpy as np

# Define the coefficients of the objective function and the constraints
c = np.array([3, 4])
b = np.array([7, 11, 8])
A = np.array([[1, 2], [3, 2], [2, 1]])

# Print the coefficients
def print_coefficients(c, A, b):
    print('Objective function coefficients: ', c)
    print('Constraint coefficients: \n', A)
    print('Right-hand side coefficients: ', b)

print_coefficients(c, A, b)

# %%
import numpy as np
from scipy.linalg import lu_factor

# Define the coefficients of the objective function and the constraints
c = np.array([3, 4])
b = np.array([7, 11, 8])
A = np.array([[1, 2], [3, 2], [2, 1]])

# Perform LU decomposition on the constraint matrix
def perform_lu_decomposition(A):
    lu, piv = lu_factor(A)
    return lu, piv

lu, piv = perform_lu_decomposition(A)
print('LU decomposition: \n', lu)
print('Pivot indices: ', piv)
