import numpy as np
import matplotlib.pyplot as plt
import os
import sys

prob_sizes = [64, 128, 256, 512]
cusparse = [0.000446, 0.002864, 0.0244, 0.2178]
ours_global = [0.00065, 0.0030, 0.0172, 0.1127]
ours_shared = [0.00039, 0.00193, 0.0111, 0.104]

plt.loglog(prob_sizes, cusparse, '-o', basey=2, basex=2, label='CUSPARSE dgtsvStridedBatch')
plt.loglog(prob_sizes, ours_global, '-o', basey=2, basex=2, label='Our solver, global memory')
plt.loglog(prob_sizes, ours_shared, '-o', basey=2, basex=2, label='Our solver, shared memory')
plt.legend(loc='best')
plt.savefig('cusparse-vs-ours-K40.png')
