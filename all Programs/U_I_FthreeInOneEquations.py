import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def model(y, t, k_UI, k_IU, k_IF, k_FI, k_FU, k_UF):
    U, I, F = y
    dU_dt = -k_UI * U + k_IU * I + k_UF * F - k_FU * U
    dI_dt = k_UI * U - k_IU * I - k_IF * I + k_FI * F
    dF_dt = k_IF * I - k_FI * F - k_UF * F + k_FU * U
    return [dU_dt, dI_dt, dF_dt]


U0 = 1.0  # mol/L
I0 = 0.0  # mol/L
F0 = 0.0  # mol/L
y0 = [U0, I0, F0]


k_UI = 1.0
k_IU = 0.5
k_IF = 1.0
k_FI = 0.5
k_FU = 1.0
k_UF = 0.5


t = np.linspace(0, 10, 1000)


result = odeint(model, y0, t, args=(k_UI, k_IU, k_IF, k_FI, k_FU, k_UF))


plt.plot(t, result[:, 0], label='[U]')
plt.plot(t, result[:, 1], label='[I]')
plt.plot(t, result[:, 2], label='[F]')
plt.xlabel('Time')
plt.ylabel('Concentration (mol/L)')
plt.legend()
plt.title('Concentration vs Time')
plt.show()
