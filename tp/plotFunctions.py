#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np


def get_number_per_values_from_dict(dict, decroissant=False):
	return sorted(dict, key=dict.get, reverse=decroissant)

def plot_occ2count(occ2count):

	x = sorted(occ2count.keys())
	# print(x)
	
	for occ in x:
		'''print(occ)'''
	y = [ occ2count[occ] for occ in x ]

	'''print(occ2count.values())'''
	fig = plt.figure()
	ax = fig.add_subplot(111)
	plt.hist(list(occ2count.values()), bins=400)
	plt.title("Word occurrence distribution")
	plt.xlabel("Number of occurrences of a wordform in a text")
	plt.ylabel("Number of wordforms with that number of occurrences")
	
	# plt.plot(x, y)
	plt.show()
	
def plot_rank2occ(tok2count):
	samplesize = len(tok2count)
	
	x_labels = get_number_per_values_from_dict(tok2count, True)[:samplesize]
	x = [ i for i in range(len(x_labels)) ]
	y = [ tok2count[tok] for tok in x_labels ]

	fig = plt.figure()
	ax = fig.add_subplot(111)
	plt.plot(x, y)
	locs, labels = plt.xticks(x, x_labels)
	plt.setp(labels, rotation=90)

	plt.tick_params(axis='x', which='major', labelsize=5)
	plt.xlabel("Wordforms sorted by frequency rank", fontsize=30)
	plt.ylabel("Number of wordforms with that number of occurrences", fontsize=30)
	fig.set_size_inches(40, 20, forward=True)
	# fig.savefig('outfile.png', dpi=200)
