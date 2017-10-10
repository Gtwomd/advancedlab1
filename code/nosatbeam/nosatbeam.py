import numpy as np
import matplotlib.pyplot as plt

t, currentamp, detectamp = np.loadtxt('../../data/day2/best001.csv', delimiter=',', unpack=True, skiprows=2)
fig, ax = plt.subplots()
spectrum = detectamp - 20*currentamp

ax.plot(t, spectrum, color='k')

ax.axvline(-.0365, ls='--', alpha=0.5, color='k')
ax.axvline(-.0318, ls='--', alpha=0.5, color='k')
ax.axvline(-.02, ls='--', alpha=0.5, color='k')
ax.axvline(-.01, ls='--', alpha=0.5, color='k')

ax.text(-.0365,9,'87b')
ax.text(-.0318,13,'85b')
ax.text(-.02,5.5,'85a')
ax.text(-.01,4,'87a')

ax.set_xlim(-.05,0)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_ylabel('amplitude')
ax.set_xlabel('phase')

plt.savefig('../../figures/nosatbeam/nosatbeam.pdf')
