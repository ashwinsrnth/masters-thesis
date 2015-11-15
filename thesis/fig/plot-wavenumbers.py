import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt

plt.style.use('bmh')

def get_wprime(w, a, b, c, alpha, beta):
    return (a*sin(w) + (b/2)*sin(2*w) + (c/3)*sin(3*2))/(1 + 2*alpha*cos(w) + 2*beta*cos(2*w))

w = np.linspace(0, np.pi, 100)
w_prime_second_central = get_wprime(w, 1.0, 0.0, 0.0, 0.0, 0.0)
w_prime_fourth_central = get_wprime(w, 4./3, -1./3, 0.0, 0.0, 0.0)
#w_prime_sixth_central = get_wprime(w, 1.0, 0.0, 0.0, 0.0, 0.0)
w_prime_pade = get_wprime(w, 3./2, 0.0, 0.0, 1./4, 0.0)
w_prime_sixth_tridiagonal = get_wprime(w, 14./9, 1./9, 0, 1./3, 0.0)
plt.plot(w, w_prime_second_central, 'k', linewidth=2, label='2nd order central')
plt.plot(w, w_prime_fourth_central, 'k:', linewidth=2, label='4th order central')
plt.plot(w, w_prime_pade, 'k--', linewidth=2, label='4th order, compact tridiagonal')
plt.plot(w, w_prime_sixth_tridiagonal, 'k-.', linewidth=2, label='6th order, compact tridiagonal')
plt.plot(w, w, 'k-', linewidth=3, label='exact')

plt.legend(loc='best')
plt.ylabel('$hk^{\prime}$')
plt.xlabel('$hk$')
plt.savefig('modified-wavenumbers.eps')
