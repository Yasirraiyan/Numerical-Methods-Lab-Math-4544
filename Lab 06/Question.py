Ordinary Differential Equation (ODE) is a differential equation consisting of one or more functions of a single independent variable and the derivatives of those functions. Finding derivatives analytically is a complex procedure, involving a lot of rules. Computers and calculators find derivatives using some sort of numerical methods. Here, our target is to estimate a function at discrete points given its differential equation using the Runge-Kutta 2nd Order method. An important thing to note here is that this method can only solve first order ODE of the form
dydx=f(x,y),y(x0)=y0 

In today's lab, we will be implementing the Runge-Kutta 2nd Order method for solving a first order ODE in python. Refer to the example in the lecture slide.

The following is the problem you need to solve.
A ball at  1200K  is allowed to cool down in air at an ambient temperature of  300K . Assuming heat is lost only due to radiation, the differential equation for the temperature of the ball is given by
dθdt=−2.2067×10−12(θ4−81×108),y(0)=1,θ(0)=1200K 
where  θ  is in  K  and  t  in seconds. Find the temperature at  t=480  seconds using Runge-Kutta 2nd Order method. Assume a step size of  h=240  seconds. Compare with the exact value.

Task 1
Implement the bivariate function f(t,θ) and the algorthim for Runge-Kutta 2nd Order method. Use the Heun's method assumption a2=12.
θi+1=θi+(12k1+12k2)h
k1=f(ti,θi)
k2=f(ti+h,θi+k1h)
where h=ti+1−ti is the step size.


[ ]

Start coding or generate with AI.

[19]
0s
import matplotlib.pyplot as plt
import numpy as np

def f(t, theta):
    return -2 * t * theta + 4 * t / theta

# Define the range for t and theta
t = np.linspace(-10, 10, 400)
theta = np.linspace(0.1, 10, 400)  # Avoid theta=0 to prevent division by zero

T, THETA = np.meshgrid(t, theta)
Z = f(T, THETA)

# Create the plot
plt.figure(figsize=(10, 6))
cp = plt.contourf(T, THETA, Z, 20, cmap='RdGy')
plt.colorbar(cp)
plt.title('$f(t, \\theta) = -2t\\theta + \\frac{4t}{\\theta}$')
plt.xlabel('t')
plt.ylabel('θ')
plt.show()



[ ]
print(f'Temperature at t = 480s with step size h = 240s is {RungeKutta2(0,1200,240,480)}K')
Your answer should be ≈584.27K.

Task 2
Calculate the exact solution of the ODE. It is the root of the nonlinear equation
0.92593ln(θ−300θ+300)−1.8519tan−1(0.333×10−2θ)=−0.22067×10−3t−2.9282
at t=480 seconds.

You can use your own root-finding algorithm or you can use the fsolve() function from the scipy package. (https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html)


[12]
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
def SolveODE(theta,t):
  return 0.92593*np.log((theta-300)/(theta+300))-1.8519*np.arctan(0.333*10**-2*theta)+0.22067*10**-3*t+2.9282
  theta_initial_guess = 600

# Solve the equation for a range of t values
t_values = np.linspace(0, 480, 100)  # 100 points from t=0 to t=480
theta_values = []

for t in t_values:
    theta_exact = fsolve(SolveODE, theta_initial_guess, args=(t))
    theta_values.append(theta_exact[0])

# Plotting the results
plt.plot(t_values, theta_values, label='Exact Solution')
plt.xlabel('Time (t) [seconds]')
plt.ylabel('Temperature (θ) [K]')
plt.title('Exact Solution of θ over Time')
plt.legend()
plt.grid(True)
plt.show()
theta_exact=SolveODE(600,480)
print(theta_exact)

t = 480
theta_initial_guess = 600
theta_exact = fsolve(SolveODE, theta_initial_guess, args=(t))
t_values = np.linspace(0, 480, 100)  
theta_values = []
print(f"The exact value of θ at t = {t} seconds is approximately {theta_exact[0]:.2f} K")


The exact value should be θexact≈647.57K.

Now, approximate the value of θ(480) using different step sizes, such as 480,240,120,60, and 30. Calculate the Global Truncation Error Et and the Absolute Relative True Error |ϵt|% in each case.


[ ]
# Write your code here.
Your values should approximately match the values of this table.
image.png

Task 3
Generate a Temperature (θ) vs Step size (h) plot which portrays the effect of step size in Runge-Kutta 2nd Order method. Use a different marker to represent the exact value.


[16]
0s
# Write your code here.
import numpy as np
import matplotlib.pyplot as plt
plt.xlabel('Step Size, h(s)')
plt.ylabel('Temparature,theta(K)')
plt.xlim(0,500)
plt.ylim(-400,800)
plt.title('Temperature  (θ)  vs Step size  (h)  plot which portrays the effect of step size in Runge-Kutta 2nd Order method. ')
h=np.linspace(0,500,100)
plt.show()


Your graph should look something like,
image.png

Genrerate a Temperature θ vs Time t plot that compares the Runge-Kutta 2nd Order method approximations for different step sizes with the exact solution.


[ ]
# Write your code here.
Your graph should look something like,
image.png

