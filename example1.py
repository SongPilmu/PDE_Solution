import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("2D heat equation solver")

plate_length = 100
max_iter_time = 750

alpha = 2
delta_x = 1

delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)

# Initialize solution: the grid of u(k, i, j) #k는 t, x는 i, y는 j
u = np.empty((max_iter_time, plate_length, plate_length))

# Initial condition everywhere inside the grid
u_initial = 0

# Set the initial condition
u.fill(u_initial)

# Boundary conditions -> 이렇게 주고 싶어서
u_top = 100.0
u_center = 100.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

# Set the boundary conditions -> 이렇게 코드를 고침 -> 왼쪽 아래부터 x,y가 0부터 시작, max_length는 50, -> 모든 k(시간)에 대해서 top은 100도(u=100)로 고정
u[:, (plate_length-1):, :] = u_top # 모든 k에 대해서 
u[:, :, :1] = u_left # 왼쪽부터 0이므로 0~1까지 섭씨 0도
u[:, :1, 1:] = u_bottom # :는 모든 원소, :1은 0부터1, 1:는 1부터 1개, 만약 2:이라면 2부터 2개
u[:, :, (plate_length-1):] = u_right
u[:, (plate_length//2)-20:(plate_length//2)+20, (plate_length//2)-20:(plate_length//2)+20] = u_center


def calculate(u):
    for k in range(0, max_iter_time-1, 1): # 아래 두줄과 같이 0~max_iter_time까지 dt만큼 증가해야하는데 여기서는 1로하고 마지막 gamma에 dt(stable조건을 만족하는)가 포함
        for i in range(1, plate_length-1, delta_x): 
            for j in range(1, plate_length-1, delta_x):
                # 삼중 배열은 안의 안의 배열의 값을 도출하기 위한 방법
                u[k + 1, i, j] = gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]

    return u

def plotheatmap(u_k, k):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap='jet', vmin=0, vmax=100) # vmin,vmax는 색의 mesh정도를 나누는 정도
    plt.colorbar()

    return plt

# Do the calculation here
u = calculate(u)

def animate(k):
    plotheatmap(u[k], k)


anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
plt.show()
anim.save("heat_equation_solution.gif")


print("Done!")