import sys
import matplotlib.pyplot as plt
from loadtxt import loadtxt

x_mult, y_mult = sys.argv[1:3]

x_mult = float(x_mult)
y_mult = float(y_mult)


t,x,y = loadtxt('best001.csv')


plt.plot(t, y_mult*y - x_mult*x)
plt.show()