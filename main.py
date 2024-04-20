import numpy as np
from scipy.interpolate import CubicSpline
import scipy.constants as C
import matplotlib.pyplot as plt
from numdifftools import Derivative

c_raw = [0,0.015, 0.03, 0.06, 0.09, 0.15, 0.3]
sigma_raw = [71.18, 68.81, 65.19, 59.32, 55.53, 49.78, 40.6]

curve = CubicSpline(c_raw, sigma_raw)

plt.figure(1, (3.42519685 * 1.5, 3.34645669 * 1.5))
plt.xlabel(r"$\frac{c}{c^θ}$")
plt.ylabel("σ (mN/m)")
c_range = np.linspace(0, 0.3, 100)
plt.plot(c_range, curve(c_range))
plt.scatter(c_raw, sigma_raw, 5, marker="s")

print("dσ/dc*cθ (mN/m): " + str(curve(c_raw, 1)))


def gamma(x):
    return - x / C.R / 303.15 * curve(x, 1) * 10000


print("Γ (nmol/m^2): " + str(gamma(np.array(c_raw))))

plt.figure(2, (3.46456693 * 1.5, 3.38582677 * 1.5))
plt.xlabel("c (mol/L)")
plt.ylabel("Γ $(nmol/m^2)$")
plt.plot(c_range, gamma(c_range))

plt.show()
