import numpy as np
import matplotlib.pyplot as plt
import matplotlib

sizes = np.array([64, 128, 256, 512, 1024, 2048])

# results on 4 nodes:
CPU_4 = np.array([0.000654, 0.00144, 0.020, 0.147, 1.09, None])
GPU_4 = np.array([0.0043, 0.0052, 0.0094, 0.034, 0.207, None])
MCPU_4 = np.array([None, 0.01, 0.034, 0.124, 0.75, None])

fig, ax = plt.subplots()
ax.plot(sizes[:-1], CPU_4[:-1], '-o', linewidth=2, label='Reference approach: 64 CPU cores')
ax.plot(sizes[:-1], GPU_4[:-1], '-o', linewidth=2, label='Cyclic reduction: 8 GPUs')
ax.plot(sizes[1:-1], MCPU_4[1:-1], '-o', linewidth=2, label='pThomas algorithm: 8 CPUs')
ax.set_xlabel('Problem size in one direction')
ax.set_ylabel('Time to solve tridiagonal system')

ax.set_yscale('log', basey=2)
ax.set_xscale('log', basex=2)
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

ax.tick_params(labelright=True)

ax.legend(loc='best')
ax.grid()
fig.savefig('4-nodes.png')
plt.close(fig)

# results on 32 nodes:
CPU_32 = np.array([None, 0.0017, 0.010, 0.028, 0.226, 1.75])
GPU_32 = np.array([None, 0.017, 0.007, 0.026, 0.084, 0.41])
MCPU_32 = np.array([None, None, 0.011, 0.046, 0.19, 1.09])

fig, ax = plt.subplots()
ax.loglog(sizes[1:], CPU_32[1:], '-o', basex=2, basey=2, linewidth=2, label='Reference approach: 512 CPU cores')
ax.loglog(sizes[1:], GPU_32[1:], '-o', basex=2, basey=2, linewidth=2, label='Cyclic reduction: 64 GPUs')
ax.loglog(sizes[2:], MCPU_32[2:], '-o', basex=2, basey=2, linewidth=2, label='pThomas algorithm: 64 CPUs')
ax.set_xlabel('Problem size in one direction')
ax.set_ylabel('Time to solve tridiagonal system')

ax.set_yscale('log', basey=2)
ax.set_xscale('log', basex=2)
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

ax.tick_params(labelright=True)

ax.legend(loc='best')

ax.grid()
fig.savefig('32-nodes.png')
plt.close(fig)




# CPU_64
# GPU_64
# MCPU_64
