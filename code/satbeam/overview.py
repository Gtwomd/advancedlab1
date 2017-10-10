import numpy as np
import matplotlib.pyplot as plt

t, nosat, sat = np.loadtxt('../../data/day3/scope_data_very_wide001.csv', delimiter=',', unpack=True, skiprows=2)
fig, ax = plt.subplots()
offset = -23.75 - (14/.04)*np.linspace(0, .04, 599)
ax.plot(t, sat - offset, color='k')
ax.set_xlim(0.01, 0.05)

ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_ylabel('amplitude')
ax.set_xlabel('phase')

# plt.show()
plt.savefig('../../figures/satbeam/overview.pdf')
