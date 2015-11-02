import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

#plt.style.use('bmh')
# 2-D plots
prob_sizes = [32, 64, 128, 256, 512., 1024, 2048]
globalmem = np.array(
        [0.201, 0.247, 0.284, 0.326, 0.403, 1.375, 5.811])
sharedmem = np.array(
        [0.024, 0.025, 0.032, 0.066, 0.273, 1.252, 10.407])

ind = np.arange(7)*2
fig, ax = plt.subplots()
width = 0.5
globalmem_bars = ax.bar(ind+0*width, globalmem, width, color='r')
sharedmem_bars = ax.bar(ind+1*width, sharedmem, width, color='g')

ax.set_yscale('log', basey=2)
ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter('%.1f'))
ax.set_xlabel('Problem size')

ax.set_xlabel('System size (Number of systems = system size)')
ax.set_ylabel('Time to solve systems (ms)')
ax.set_xticks(ind+width)
ax.set_xticklabels( 
    ('$32$', '$64$', '$128$', '$256$', '$512$', '$1024$', '$2048$') )
ax.tick_params(labelright=True)
ax.set_title('Global v/s shared memory solver performance for 2-D problems')
ax.grid(True)
leg = ax.legend((
            globalmem_bars[0],
            sharedmem_bars[0]),
            ('Global memory',
            'Shared memory'),
            loc='best',
            fontsize='medium')
leg.draw_frame(True)
plt.savefig('global-vs-shared-2d.eps')

#plt.style.use('bmh')
# 3-D plots
prob_sizes = [32, 64, 128, 256, 512]
globalmem = np.array(
        [0.207, 0.751, 3.669, 21.148, 145.34])
sharedmem = np.array(
        [0.092, 0.409, 2.225, 12.565, 125.311])

ind = np.arange(5)*2
fig, ax = plt.subplots()
width = 0.5
globalmem_bars = ax.bar(ind+0*width, globalmem, width, color='r')
sharedmem_bars = ax.bar(ind+1*width, sharedmem, width, color='g')

ax.set_yscale('log', basey=2)
ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter('%.1f'))
ax.set_xlabel('Problem size')

ax.set_xlabel('System size (Number of systems = system size$^2$)')
ax.set_ylabel('Time to solve systems (ms)')
ax.set_xticks(ind+width)
ax.set_xticklabels( 
    ('$32$', '$64$', '$128$', '$256$', '$512$', '$1024$', '$2048$') )
ax.tick_params(labelright=True)
ax.set_title('Global v/s shared memory solver performance for 3-D problems')
ax.grid(True)
leg = ax.legend((
            globalmem_bars[0],
            sharedmem_bars[0]),
            ('Global memory',
            'Shared memory'),
            loc='best',
            fontsize='medium')
leg.draw_frame(True)
plt.savefig('global-vs-shared-3d.eps')
