import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

plt.style.use('bmh')

ngpus = np.array([1, 4, 27, 64])

# size per proc = 128
dfdx = np.array([
    2.117, 5.12, 5.49, 6.20])
dfdy = np.array([
    2.66, 5.15, 5.53, 5.73])
dfdz = np.array([
    2.96, 5.53, 5.93, 6.32])

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
ax.set_xticklabels(['1', '8', '27', '64'])
ax.legend(loc='best')
ax.set_xlabel('Number of GPUs')
ax.set_ylabel('Time to solve in ms')
ax.set_xlim((-0.1, 3.2))
plt.savefig('weak-scaling-128.eps')

ngpus = np.array([1, 4, 64])

# prob size: 256
dfdx = np.array([
    12.41, 22.9, 24.4])
dfdy = np.array([
    17.30, 26.7, 30.0])
dfdz = np.array([
    19.30, 28.8, 40.0])

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
ax.legend(loc='best')
ax.set_xlabel('Number of GPUs')
ax.set_ylabel('Time to solve in ms')
ax.set_xlim((-0.1, 2.2))
plt.savefig('weak-scaling-256.eps')
