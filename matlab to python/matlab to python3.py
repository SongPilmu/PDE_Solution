import numpy as np
import matplotlib as plt

N=100
dx = 1/N
A_diag = np.eye(N-1) * (-4 / dx**2)
A_diag = A_diag + np.eye(N-1,N-1,k=1)/dx**2
A_diag = A_diag + np.eye(N-1,N-1,k=-1)/dx**2
print(A_diag)
