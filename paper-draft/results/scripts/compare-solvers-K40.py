import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys


plt.style.use('bmh')
prob_sizes = [64, 128, 256, 512]
intel_mkl = np.array([1.13, 8.90, 77.67, 654])
cusparse = np.array([0.000446, 0.002864, 0.0244, 0.2178])*1000
ours_global = np.array([0.00065, 0.0030, 0.0172, 0.1127])*1000
ours_shared = np.array([0.00039, 0.00193, 0.0111, 0.104])*1000

ind = np.arange(4)*2
fig, ax = plt.subplots()
width = 0.25
mkl_bars = ax.bar(ind, intel_mkl, width, color='r')
cusparse_bars = ax.bar(ind+width, cusparse, width, color='b')
global_bars = ax.bar(ind+2*width, ours_global, width, color='y')
shared_bars = ax.bar(ind+3*width, ours_shared, width, color='g')

ax.set_yscale('log')
ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())
ax.set_xlabel('Problem size')
ax.set_ylabel('Time (ms)')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('$64^3$', '$128^3$', '$256^3$', '$512^3$') )
ax.tick_params(labelright=True)
ax.set_title('Performance of solvers on Tesla K40')
ax.grid(True)
leg = ax.legend( (mkl_bars[0],
            cusparse_bars[0],
            global_bars[0],
            shared_bars[0]),
            ('Intel MKL', 'CUSPARSE',
             'Our solver (global memory)',
             'Our solver (shared memory)'), loc='best')
leg.draw_frame(False)
plt.savefig('compare-solvers-K40.eps')
