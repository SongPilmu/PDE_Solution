import numpy as np
from matplotlib import pyplot as plt

# Grid point
N = 100
x = np.linspace(0,1,num=N-1)
dx = x[1]-x[0]

#Kappa 확산계수
K = 0.01

# 초기 변위값 1로 설정
U = np.ones((N-1,1))

#Neumann stability time grid 
dt = 0.0001

# A 행렬 계산
A_diag = np.eye(N-1) * (-2/dx**2)
A_diag = A_diag + np.eye(N-1,N-1,k=1) * (1/dx**2)
A_diag = A_diag + np.eye(N-1,N-1,k=-1) * (1/dx**2)

# B 행렬 계산
B = np.array([0,0,0,0,0,0,0,0,0])

print(1/dt)

# 총 10번 반복
for i in range(1,int((1/dt))):
    U = U + (K * (np.dot(A_diag,U) + B) * dt)
    # print(U)

plt.plot(x,U)
plt.xlabel('time')
plt.ylabel('displacement')
plt.title('Heat equation Result')
plt.show()