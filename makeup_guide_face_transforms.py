'''
Given a list of 4x4 face transform matrices, prints the range of each value in
the matrix and plots the ones that vary a lot.
'''

import numpy as np
from matplotlib import pyplot as plt


tolerance = 0.07

FILE_NAMES = ['horizontal_centering_data_1.txt',
			  'horizontal_sweep_data_1.txt',
			  'vertical_centering_data_1.txt',
			  'vertical_sweep_data_1.txt']


def plot_transforms(transform_matrices, file_name):
	'''
	Given a list of 4x4 transform matrices, plots each value in the matrix.
	There should be 16 graphs in total, one for each value in the 4x4.

	Args:
	transform_matrices: a numpy array representing a list of 4x4 transform
		matrices.
	'''
	for i in range(4):
		plt.figure(i+1)
		for j in range(4):
			plot_transform(transform_matrices[0:,i,j], f"[{i},{j}]", file_name)


def plot_transform(transform_values, plot_number, file_name):
	'''
	Plots an array of values, with the minimum and maximum listed on the plot.
	Note: it only plots if the values differ significantly.

	Args:
	transform_values: a 1D array representing all values for one position in
		each transform matrix. Ex: all values for position [0][0]
	plot_number: a string representing which position is being plotted
	'''
	max = transform_values.max()
	min = transform_values.min()
	if max-min >= tolerance:
		plt.plot(range(len(transform_values)), transform_values, label=plot_number)
		plt.ylim([-1,1])
		plt.legend()
		plt.title(file_name)
	print(f"{plot_number}, max: {max}, min: {min}")


def plot_from_file(file_name):
	data = np.array([])
	with open(file_name, 'r') as file:
		# convert string to array
		content = file.read()
		content = content.replace("[[[", "").replace("]]]", "")
		content = content.split("]]\n[[")
		for i, matrix in enumerate(content):
			content[i] = matrix.split("], [")
			for j, line in enumerate(content[i]):
				content[i][j] = line.split(", ")

		# convert array to numpy array
		data = np.array(content).astype(np.float64)

	plot_transforms(data, file_name)
	plt.show()


# plot_from_file(FILE_NAMES[0])
