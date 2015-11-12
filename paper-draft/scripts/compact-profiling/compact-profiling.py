import numpy as np
import pandas
import matplotlib
import matplotlib.pyplot as plt
import os
import sys
import collections



plt.style.use('bmh')
fig, ax = plt.subplots()

# horizontal bar with timing breakdown

# size 256, 64 GPUs
results_lists = [
 [6.640, 2.700, 12.864, 5.336, 2.869, 0],
 [6.322, 2.771, 12.729, 5.427, 2.708, 6.226],
 [6.515, 2.721, 12.892, 5.465, 2.536, 8.679]]

df = pandas.DataFrame(results_lists, index=['dfdx', 'dfdy', 'dfdz'],
    columns=['Halo swaps', 'RHS', 'Primary systems', 'Reduced systems', 'Summing solutions', 'Permutations'])
df.plot(kind='bar', stacked=True, ax=ax)
leg=plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
ax.set_ylabel('Time taken (ms)')
ax.set_xticklabels(df.index, rotation=0)
plt.savefig('profiling-1024-64.eps', extra_artists=(leg,), bbox_inches='tight')
plt.close()

fig, ax = plt.subplots()

# size 512, 64 GPUs
results_lists = [
[35.43, 16.88, 98.97, 10.63, 13.68, 0],
[35.69, 16.84, 98.43, 6.83, 13.66, 41.53],
[34.47, 16.83, 99.00, 6.74, 13.67, 52.08]]
df = pandas.DataFrame(results_lists, index=['dfdx', 'dfdy', 'dfdz'],
    columns=['Halo swaps', 'RHS', 'Primary systems', 'Reduced systems', 'Summing solutions', 'Permutations'])
df.plot(kind='bar', stacked=True, ax=ax)
leg=plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
ax.set_ylabel('Time taken (ms)')
ax.set_xticklabels(df.index, rotation=0)
plt.savefig('profiling-2048-64.eps', bbox_extra_artists=(leg,), bbox_inches='tight')

