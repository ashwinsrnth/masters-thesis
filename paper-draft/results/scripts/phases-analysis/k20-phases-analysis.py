import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

plt.style.use('bmh')
# 3-D plots
prob_sizes = [32, 64, 128, 256, 512]

forward_globalmem = np.array(
        [0.105, 0.317, 1.585, 9.645, 68.635])
solve_globalmem = np.array(
        [0.026, 0.057, 0.226, 0.883, 3.526])
backward_globalmem = np.array(
        [0.103, 0.373, 1.850, 10.588, 73.086])
forward_sharedmem = np.array(
        [0.031, 0.136, 0.758, 3.523, 35.192])
solve_sharedmem = np.array(
        [0.024, 0.069, 0.256, 1.084, 8.520])
backward_sharedmem = np.array(
        [0.065, 0.313, 1.484, 7.382, 70.943])

forward_globalmem_percent = forward_globalmem/(
        forward_globalmem+backward_globalmem+solve_globalmem)*100
solve_globalmem_percent = solve_globalmem/(
        forward_globalmem+backward_globalmem+solve_globalmem)*100
backward_globalmem_percent = backward_globalmem/(
        forward_globalmem+backward_globalmem+solve_globalmem)*100
forward_sharedmem_percent = forward_sharedmem/(
        forward_sharedmem+backward_sharedmem+solve_sharedmem)*100
solve_sharedmem_percent = solve_sharedmem/(
        forward_sharedmem+backward_sharedmem+solve_sharedmem)*100
backward_sharedmem_percent = backward_sharedmem/(
        forward_sharedmem+backward_sharedmem+solve_sharedmem)*100


ind = np.arange(5)*2
fig, ax = plt.subplots(figsize=(8, 8))
width = 0.5
forward_globalmem_bars = ax.barh(
        ind+0*width, forward_globalmem_percent, width, color='b')
solve_globalmem_bars = ax.barh(
        ind+0*width, solve_globalmem_percent, width,
        left=forward_globalmem_percent, color='r')
backward_globalmem_bars = ax.barh(
        ind+0*width, backward_globalmem_percent, width,
        left=solve_globalmem_percent+forward_globalmem_percent, color='g')
forward_sharedmem_bars = ax.barh(
        ind+1*width, forward_sharedmem_percent, width, color='b')
solve_sharedmem_bars = ax.barh(
        ind+1*width, solve_sharedmem_percent, width,
        left=forward_sharedmem_percent, color='r')
backward_sharedmem_bars = ax.barh(
        ind+1*width, backward_sharedmem_percent, width,
        left=solve_sharedmem_percent+forward_sharedmem_percent, color='g')

ax.get_xaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())
ax.xaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter('%.1f'))
ax.set_ylabel('Problem size')

ax.set_ylabel('System size (Number of systems = system size$^2$)')
ax.set_xlabel('Percentage of total solver time')
ax.set_yticks(ind+width)
ax.set_yticklabels( 
    ('32', '64', '128', '256', '512', '1024', '2048') )
ax.set_xticks(range(10, 120, 10))
ax.set_xticklabels( 
    ('10', '20', '30', '40', '50', '60', '70', '80', '90', '100') )
ax.set_title('Breakdown of solver runtime')
ax.grid(True)
leg = ax.legend((
            forward_globalmem_bars[0],
            solve_globalmem_bars[0],
            backward_globalmem_bars[0]),
            ('Forward reduction',
            '2x2 solve',
            'Backward substitution'),
            loc='best',
            fontsize='medium',
            bbox_to_anchor=(0.5, 1.1))
leg.draw_frame(True)
plt.savefig('k20-phases-analysis.eps', bbox_extra_artists=(leg,), bbox_inches='tight')
