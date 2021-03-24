import numpy as np
from matplotlib import pyplot as plt

# Grid point
N = 25
x = np.linspace(0,1,num=N-1)
dx = x[1]-x[0]
dt = 0.001
U = 0.5


A_diag = np.eye(N-1,N-1,k=1) * (1/dx**2)
A_diag = A_diag + np.eye(N-1,N-1,k=-1) * (-1/dx**2)
A_diag[0][N-2] = 1/2*dx
A_diag[N-2][0] = -1/2*dx

B = np.zeros((N-1,1))

u = np.exp(-(-x-0.5)**2/0.1**2)

for i in range(1,int((1/dt))):
    u = u + (-U * (np.dot(A_diag,u) + B) * dt)

print(A_diag)
print(B)
print(u)

plt.plot(x,u)
plt.show()
