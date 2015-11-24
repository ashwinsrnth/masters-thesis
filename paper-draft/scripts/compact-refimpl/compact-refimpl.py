import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')

sizes = [256, 512, 1024, 2048]

cpu_8 = np.array([79.5, 556.8, 5188, np.nan])
cpu_64 = np.array([20.8, 146.5, 1092, np.nan])
cpu_512 = np.array([11.1, 29.2, 223.7, 1741.])

gpu_1 = np.array([19.9, 164.5, np.nan, np.nan])
gpu_8 = np.array([5.17, 23.24, 174.9, np.nan])
gpu_64 = np.array([2.79, 5.62, 24.49, 297.07])

speedup_1 = cpu_8/gpu_1
speedup_8 = cpu_64/gpu_8
speedup_64 = cpu_512/gpu_64

ind = np.arange(4)*2
fig, ax = plt.subplots()
width = 0.5

speedup_1_bars = ax.bar(ind+0*width, speedup_1, width, color='c')
speedup_8_bars = ax.bar(ind+1*width, speedup_8, width, color='m')
speedup_64_bars = ax.bar(ind+2*width, speedup_64, width, color='y')

ax.set_xticks(ind+1.5*width)
ax.set_xticklabels(['$256^3$', '$512^3$',
    '$1024^3$', '$2048^3$'])
ax.set_xlabel('Problem size')
ax.set_ylabel('Speedup over reference implementation')
ax.grid(True)

leg = ax.legend((
            speedup_1_bars,
            speedup_8_bars,
            speedup_64_bars),
            ('1 socket',
             '8 sockets',
             '64 sockets'),
            loc='best',
            fontsize='medium')
leg.draw_frame(True)
plt.savefig('compact-refimpl-speedups.eps')
