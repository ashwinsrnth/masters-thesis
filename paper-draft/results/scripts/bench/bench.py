import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

plt.style.use('bmh')
# 2-D plots
prob_sizes = [32, 64, 128, 256, 512., 1024, 2048]
intel_mkl_1 = np.array(
        [0.045, 0.048, 0.089, 0.263, 0.959, 3.775, 16.272])
intel_mkl_2 = np.array(
        [0.043, 0.052, 0.086, 0.217, 0.688, 2.612, 10.953])
intel_mkl_4 = np.array(
        [0.045, 0.051, 0.068, 0.151, 0.412, 1.577, 6.815])
intel_mkl_8 = np.array(
        [0.042, 0.048, 0.084, 0.107, 0.299, 1.023, 4.823])
intel_mkl_16 = np.array(
        [0.050, 0.249, 0.145, 0.202, 0.299, 0.864, 4.111])
cusparse = np.array(
        [0.273, 0.271, 0.271, 0.305, 0.629, 1.939, 7.607])
neato_shared = np.array(
        [0.024, 0.025, 0.032, 0.066, 0.272, 1.252, 10.407])
matrix = np.vstack([intel_mkl_1,
                    intel_mkl_2,
                    intel_mkl_4,
                    intel_mkl_8,
                    intel_mkl_16,
                    cusparse,
                    neato_shared])
mins = np.min(matrix, axis=0)

# normalize timings:
intel_mkl_1 = intel_mkl_1/mins
intel_mkl_2 = intel_mkl_2/mins
intel_mkl_4 = intel_mkl_4/mins
intel_mkl_8 = intel_mkl_8/mins
intel_mkl_16 = intel_mkl_16/mins
cusparse = cusparse/mins
neato_shared = neato_shared/mins

ind = np.arange(7)*5
fig, ax = plt.subplots()
width = 0.5
mkl_1_bars = ax.bar(ind+0*width, intel_mkl_1, width, color='r')
mkl_2_bars = ax.bar(ind+1*width, intel_mkl_2, width, color='g')
mkl_4_bars = ax.bar(ind+2*width, intel_mkl_4, width, color='b')
mkl_8_bars = ax.bar(ind+3*width, intel_mkl_8, width, color='orange')
mkl_16_bars = ax.bar(ind+4*width, intel_mkl_16, width, color='m')
cusparse_bars = ax.bar(ind+5*width, cusparse, width, color='y')
neato_bars = ax.bar(ind+6*width, neato_shared, width, color='c')

ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter('%d'))

ax.set_xticks(ind+3*width)
ax.set_xticklabels(['32', '64', '128', '256', '512', '1024', '2048'])
ax.set_xlabel('Problem size')

ax.set_xlabel('System size (Number of systems = system size)')
ax.set_ylabel('Relative time to solve systems')
ax.tick_params(labelright=True)
ax.grid(True)
leg = ax.legend((
            mkl_1_bars[0],
            mkl_2_bars[0],
            mkl_4_bars[0],
            mkl_8_bars[0],
            mkl_16_bars[0],
            cusparse_bars[0],
            neato_bars[0]),
            ('Intel MKL 1 core',
            'Intel MKL 2 cores',
            'Intel MKL 4 cores',
            'Intel MKL 8 cores',
            'Intel MKL 16 cores',
            'CUSPARSE',
            'NEATO solver'),
            loc='best',
            fontsize='medium')
leg.draw_frame(True)
plt.savefig('bench-2d.eps')

#plt.style.use('bmh')
# 3-D plots
prob_sizes = [32, 64, 128, 256, 512]
intel_mkl_1 = np.array(
        [0.152, 0.879, 7.052, 63.858, 515.792])
intel_mkl_2 = np.array(
        [0.132, 0.834, 6.504, 38.724, 298.401])
intel_mkl_4 = np.array(
        [0.099, 0.493, 3.864, 24.430, 194.107])
intel_mkl_8 = np.array(
        [0.094, 0.306, 2.553, 18.792, 196.748])
intel_mkl_16 = np.array(
        [0.257, 0.403, 1.931, 16.610, 159.394])
cusparse = np.array(
        [0.310, 0.556, 3.128, 28.495, np.inf])
neato_shared = np.array(
        [0.093, 0.409, 2.224, 12.568, 125.326])

matrix = np.vstack([intel_mkl_1,
                    intel_mkl_2,
                    intel_mkl_4,
                    intel_mkl_8,
                    intel_mkl_16,
                    cusparse,
                    neato_shared])
mins = np.min(matrix, axis=0)

# normalize timings:
intel_mkl_1 = intel_mkl_1/mins
intel_mkl_2 = intel_mkl_2/mins
intel_mkl_4 = intel_mkl_4/mins
intel_mkl_8 = intel_mkl_8/mins
intel_mkl_16 = intel_mkl_16/mins
cusparse = cusparse/mins
neato_shared = neato_shared/mins

ind = np.arange(5)*5
fig, ax = plt.subplots()
width = 0.5
mkl_1_bars = ax.bar(ind+0*width, intel_mkl_1, width, color='r')
mkl_2_bars = ax.bar(ind+1*width, intel_mkl_2, width, color='g')
mkl_4_bars = ax.bar(ind+2*width, intel_mkl_4, width, color='b')
mkl_8_bars = ax.bar(ind+3*width, intel_mkl_8, width, color='orange')
mkl_16_bars = ax.bar(ind+4*width, intel_mkl_16, width, color='m')
cusparse_bars = ax.bar(ind+5*width, cusparse, width, color='y')
neato_bars = ax.bar(ind+6*width, neato_shared, width, color='c')

ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter('%d'))
ax.set_xticks(ind+3*width)
ax.set_xticklabels(['32', '64', '128', '256', '512'])
ax.set_xlabel('Problem size')

ax.set_xlabel('System size (Number of systems = system size$^2$)')
ax.set_ylabel('Relative time to solve systems')
ax.tick_params(labelright=True)
ax.grid(True)
leg = ax.legend((
            mkl_1_bars[0],
            mkl_2_bars[0],
            mkl_4_bars[0],
            mkl_8_bars[0],
            mkl_16_bars[0],
            cusparse_bars[0],
            neato_bars[0]),
            ('Intel MKL 1 core',
            'Intel MKL 2 cores',
            'Intel MKL 4 cores',
            'Intel MKL 8 cores',
            'Intel MKL 16 cores',
            'CUSPARSE',
            'NEATO solver'),
            loc='best',
            fontsize='medium')
leg.draw_frame(True)
plt.savefig('bench-3d.eps')


