import numpy as np

def loadtxt(file):
	data = np.loadtxt(file, delimiter=',', unpack=True, skiprows=1)
	return data
