import numpy as np
import matplotlib.pyplot as plt

t, michint, sat = np.loadtxt('../../data/day5/rightzoom001.csv', delimiter=',', unpack=True, skiprows=2)
fig, ax = plt.subplots()
# plot = sat - 20*nosat
ax.plot(t, sat, color='k')
ax.plot(t, michint + .04, color='k')
# ax.set_xlim(0.01, 0.05)

vlines = [.00414, .004378, .004613]

for line in vlines:
    ax.axvline(line,alpha = 0.25, color='k')

ax.axvline(.00414,alpha = 0.5, color='k')
ax.text(.00414, -.25, '85b', horizontalalignment='right')
ax.axvline(.004658,alpha = 0.5, color='k')
ax.text(.004658, -.25, '87b', horizontalalignment='right')

ax.annotate(s='', xy=(.00414,-.10), xytext=(.004658,-.10), arrowprops=dict(arrowstyle='<->'))
ax.text(.00439, -.09, '11 cycles',horizontalalignment='center')
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_ylabel('amplitude')
ax.set_xlabel('phase')
# plt.show()
plt.savefig('../../figures/michint/michintright.pdf')
