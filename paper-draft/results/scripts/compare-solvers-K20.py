import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

plt.style.use('bmh')
prob_sizes = [64, 128, 256, 512]
intel_mkl_2 = np.array([0.97, 5.884, 75.16, 703.38])
intel_mkl_4 = np.array([0.836, 7.10, 50.24, 392.7])
intel_mkl_16 = np.array([1.522, 2.84, 19.64, 221.0])
cusparse = np.array([0.000520, 0.00335, 0.0286, np.nan])*1000
ours_global = np.array([0.0008, 0.00376, 0.0213, 0.1456])*1000
ours_shared = np.array([0.000476, 0.00237, 0.0136, 0.1325])*1000

ind = np.arange(4)*2
fig, ax = plt.subplots()
width = 0.2
mkl_2_bars = ax.bar(ind, intel_mkl_2, width, color='y')
mkl_4_bars = ax.bar(ind+width, intel_mkl_4, width, color='b')
mkl_16_bars = ax.bar(ind+2*width, intel_mkl_16, width, color='c')
cusparse_bars = ax.bar(ind+3*width, cusparse, width, color='m')
global_bars = ax.bar(ind+4*width, ours_global, width, color='r')
shared_bars = ax.bar(ind+5*width, ours_shared, width, color='g')

ax.set_yscale('log', basey=2)
ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())

ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))
ax.set_xlabel('Problem size')
ax.set_ylabel('Time (ms)')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('$64^3$', '$128^3$', '$256^3$', '$512^3$') )
ax.tick_params(labelright=True)
ax.set_title('Performance of solvers on Tesla K20')
ax.grid(True)
leg = ax.legend((mkl_2_bars[0],
            mkl_4_bars[0],
            mkl_16_bars[0],
            cusparse_bars[0],
            global_bars[0],
            shared_bars[0]),
            ('Intel MKL 2 cores',
            'Intel MKL 4 cores',
            'Intel MKL 16 cores',
            'CUSPARSE',
            'Our solver (global memory)',
            'Our solver (shared memory)'),
            loc='best',
            fontsize='medium')
leg.draw_frame(False)
plt.savefig('compare-solvers-K20.eps')
