import numpy as np
import matplotlib.pyplot as plt

t, nosat, sat = np.loadtxt('../../data/day5/left001.csv', delimiter=',', unpack=True, skiprows=2)
fig, ax = plt.subplots()
# plot = sat - 20*nosat
ax.plot(t, sat, color='k')
ax.plot(t, nosat, color='k')
# ax.set_xlim(0.01, 0.05)

vlines = [.00155,.001805,.00207,.002317,.00255868, .002801]

for line in vlines:
    ax.axvline(line,alpha = 0.25, color='k')

ax.axvline(.00155,alpha = 0.5, color='k')
ax.text(.00154, -.17, '87a',horizontalalignment='right')
ax.axvline(.002774,alpha = 0.5, color='k')
ax.text(.00276, -.17, '85a', horizontalalignment='right')

ax.annotate(s='', xy=(.00155,-.14), xytext=(.002774,-.14), arrowprops=dict(arrowstyle='<->'))
ax.text(.00219, -.13, '24.5 +/- 0.5\ncycles',horizontalalignment='center')
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_ylabel('amplitude')
ax.set_xlabel('phase')
# plt.show()
plt.savefig('../../figures/michint/michintleft.pdf')
