#type "/opt/homebrew/bin/python3 -m pip install numpy" in your terminal if it doesn't work
#also type "/opt/homebrew/bin/python3 -m pip install matplotlib scipy"
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the system of ODEs
def model(y, t, k_F, k_U):
    U, F = y
    dU_dt = -k_F * U + k_U * F
    dF_dt = k_F * U - k_U * F
    return [dU_dt, dF_dt]

# Initial conditions
U0 = 1.0  # mol/L
F0 = 0.0  # mol/L
y0 = [U0, F0]

# Rate constants
k_F = 1.0  # Assuming a value, can be changed #for user input, use the code "k_F = float(input("Please enter the k_F: "))"
k_U = 0.5  # Assuming k_F > k_U #for user input, use the code "k_U = float(input("Please enter the k_U: "))"

# Time points
t = np.linspace(0, 10, 1000)  # You can adjust the time range and points as needed

# Solve the ODE
result = odeint(model, y0, t, args=(k_F, k_U))

# Plotting
plt.plot(t, result[:, 0], label='[U]')
plt.plot(t, result[:, 1], label='[F]')
plt.xlabel('Time')
plt.ylabel('Concentration (mol/L)')
plt.legend()
plt.title('Concentration vs Time')
plt.show()

# Steady state approximation for [F] at t = infinity
# At steady state, d[F]/dt = 0 => k_F * [U] = k_U * [F]
# Given [U] + [F] = U0 (conservation of mass)
# Solving the above equations, we get:
F_infinity = k_F * U0 / (k_F + k_U)
print(f"[F] at t = infinity: {F_infinity:.4f} mol/L")
