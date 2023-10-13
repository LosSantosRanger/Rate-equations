import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(y, t, k_UI, k_IF, k_FU):
    U, I, F = y
    dU_dt = -k_UI * U + k_FU * F
    dI_dt = k_UI * U - k_IF * I
    dF_dt = k_IF * I - k_FU * F
    return [dU_dt, dI_dt, dF_dt]


U0 = 1.0  # mol/L
I0 = 0.0  # mol/L
F0 = 0.0  # mol/L
y0 = [U0, I0, F0]

k_UI = 1.0
k_IF = 1.0
k_FU = 1.0


t = np.linspace(0, 10, 1000)


result = odeint(model, y0, t, args=(k_UI, k_IF, k_FU))


plt.plot(t, result[:, 0], label='[U]')
plt.plot(t, result[:, 1], label='[I]')
plt.plot(t, result[:, 2], label='[F]')
plt.xlabel('Time')
plt.ylabel('Concentration (mol/L)')
plt.legend()
plt.title('Concentration vs Time')
plt.show()
