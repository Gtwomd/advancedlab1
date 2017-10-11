import numpy as np
import matplotlib.pyplot as plt

t, michint, sat = np.loadtxt('../../data/day5/wide001.csv', delimiter=',', unpack=True, skiprows=2)
fig, ax = plt.subplots()
# plot = sat - 20*nosat
ax.plot(t, sat, color='k')
ax.plot(t, michint + .04, color='k')
ax.set_xlim(0.001, 0.005)

ax.axvline(.001545,alpha = 0.5, color='k')
ax.text(.00153, -.25, '87a', horizontalalignment='right')

ax.annotate(s='', xy=(.001545,-.10), xytext=(.00277,-.10), arrowprops=dict(arrowstyle='<->'))
ax.text(.00214, -.09, '24.5 cycles',horizontalalignment='center')

ax.axvline(.00277,alpha = 0.5, color='k')
ax.text(.00276, -.25, '85a', horizontalalignment='right')

ax.annotate(s='', xy=(.00277,-.10), xytext=(.004116,-.10), arrowprops=dict(arrowstyle='<->'))
ax.text(.00350, -.09, '28 cycles',horizontalalignment='center')

ax.axvline(.004116,alpha = 0.5, color='k')
ax.text(.00410, -.25, '85b', horizontalalignment='right')

ax.annotate(s='', xy=(.004116,-.10), xytext=(.004639,-.10), arrowprops=dict(arrowstyle='<->'))
ax.text(.00436, -.09, '11 cycles',horizontalalignment='center')

ax.axvline(.004639,alpha = 0.5, color='k')
ax.text(.00463, -.25, '87b', horizontalalignment='right')

ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_ylabel('amplitude')
ax.set_xlabel('phase')
# plt.show()
plt.savefig('../../figures/michint/michintwide.pdf')
