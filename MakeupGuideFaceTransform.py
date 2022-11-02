'''
Given a list of 4x4 face transform matrices, finds the range of each value in
the matrix and plots them individually. Also on each plot is the range of
values for easy reference.
'''

import numpy as np
from matplotlib import pyplot as plt


FILE_NAME = 'horizontal_centering_data.txt'


def plot_transforms(transform_matrices):
	'''
	Given a list of 4x4 transform matrices, plots each value in the matrix.
	There should be 16 graphs in total, one for each value in the 4x4.

	Args:
	transform_matrices: a numpy array representing a list of 4x4 transform
		matrices.
	'''
	for i in range(4):
		plt.figure(i)
		for j in range(4):
			plot_transform(transform_matrices[0:,i,j], f"[{i},{j}]")


def plot_transform(transform_values, plot_number):
	'''
	Plots an array of values, with the minimum and maximum listed on the plot.

	Args:
	transform_values: a 1D array representing all values for one position in
		each transform matrix. Ex: all values for position [0][0]
	plot_number: a string representing which position is being plotted
	'''
	plt.plot(range(len(transform_values)), transform_values, label=plot_number)
	find_max_min(transform_values, plot_number)


def find_max_min(transform_values, plot_number):
	'''
	Prints the max and min values for each column set.
	'''
	max = transform_values.max()
	min = transform_values.min()
	print(f"{plot_number}, max: {max}, min: {min}")


data = np.array([])
with open(FILE_NAME, 'r') as file:
	# convert string to array
	content = file.read()
	content = content.replace("[[[", "").replace("]]]", "")
	content = content.split("]]\n[[")
	for i, matrix in enumerate(content):
		content[i] = matrix.split("], [")
		for j, line in enumerate(content[i]):
			content[i][j] = line.split(", ")

	# convert array to numpy array
	data = np.array(content).astype(np.float)


plot_transforms(data)
plt.ylim([-1,1])
plt.legend()
plt.show()
