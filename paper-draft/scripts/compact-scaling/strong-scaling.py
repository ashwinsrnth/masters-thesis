import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

plt.style.use('bmh')

ngpus = np.array([1, 2, 3])


# prob size:  256
dfdx = np.array([
    12.5, 5.13, 2.7])
dfdy = np.array([
    17.2, 5.17, 2.87])
dfdz = np.array([
    19.2, 5.93, 2.803])

fig, ax = plt.subplots()
ax.set_yscale("log", nonposy='clip')
ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter('%d'))

ax.set_xscale("linear")
ax.plot(dfdx, 'o-', label='dfdx')
ax.plot(dfdy, 'o-', label='dfdy')
ax.plot(dfdz, 'o-', label='dfdz')
ax.set_xticks(range(len(ngpus)))
ax.set_xticklabels(['1', '8', '64'])
ax.legend()
ax.set_xlabel('Number of GPUs')
ax.set_ylabel('Time to solve in ms')
ax.set_xlim((-0.1, 2.2))
plt.savefig('strong-scaling-256.eps')

# prob size: 512
dfdx = np.array([
    114.0, 22.8, 6.2])
dfdy = np.array([
    155.0, 26.3, 5.7])
dfdz = np.array([
    166.0, 29.1, 6.3])

fig, ax = plt.subplots()
ax.set_yscale("log", nonposy='clip')
ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter('%d'))
ax.set_xscale("linear")
ax.plot(dfdx, 'o-', label='dfdx')
ax.plot(dfdy, 'o-', label='dfdy')
ax.plot(dfdz, 'o-', label='dfdz')
ax.set_xticks(range(len(ngpus)))
ax.set_xticklabels(['1', '8', '64'])
ax.legend()
ax.set_xlabel('Number of GPUs')
ax.set_ylabel('Time to solve in ms')
ax.set_xlim((-0.1, 2.2))
plt.savefig('strong-scaling-512.eps')
