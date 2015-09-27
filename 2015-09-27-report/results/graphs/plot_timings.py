import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def plot_stacked_bar(offs, width, values, colors):
    y = 0
    for color, value in zip(colors, values):
        p = plt.bar(offs, value, width, bottom=y, color=color)
        y += value

sizes = np.array([512, 1024, 2048])

CPU_512_64 = np.array([0.0096, 0.1375])
CPU_1024_64 =
CPU_2048_64 = 

CPU_512_512 = np.array([0.0044, 0.02465])
GPU_512_8 = np.array([0.02157, 0.01, 0.0035])
GPU_512_64 = np.array([0.0064, 0.018, 0.0015])
MCPU_512_8 = np.array([0.0844, 0.0205, 0.0225])
MCPU_512_64 = np.array([0.03, 0.0068, 0.00437])

plot_stacked_bar(1, 0.2, CPU_512_64, ['g', 'r'])
plot_stacked_bar(2, 0.2, CPU_512_512, ['g', 'r'])

plt.savefig('example.png')
plt.close()
