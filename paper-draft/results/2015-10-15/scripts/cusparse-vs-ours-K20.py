import numpy as np
import matplotlib.pyplot as plt
import os
import sys

prob_sizes = [64, 128, 256, 512]
cusparse = [0.000520, 0.00335, 0.0286, None]
ours_global = [0.0008, 0.00376, 0.0213, 0.1456]
ours_shared = [0.000476, 0.00237, 0.0136, 0.1325]

pt.loglog(prob_sizes, cusparse, '-o', basey=2, basex=2, label='CUSPARSE dgtsvStridedBatch')
plt.loglog(prob_sizes, ours_global, '-o', basey=2, basex=2, label='Our solver, global memory')
plt.loglog(prob_sizes, ours_shared, '-o', basey=2, basex=2, label='Our solver, shared memory')
plt.legend(loc='best')
plt.savefig('cusparse-vs-ours-K20.png')
