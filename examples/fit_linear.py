
import glob
import os
import numpy
import json

import lib.polyfit_linear as linear_fit
from lib.helpers_file import load_source_files, getFileinfo, writeToJson
from lib.helpers_plot import addDefaultGridlines, newPlot

files = load_source_files()
# index = 0

for path in files:

	samples = numpy.loadtxt(path, skiprows=4, usecols=(1,2))
	# file contains a list of x and y values per entry.
	# transpose restructures it into a list of x values and a list of y values.
	xySamples = numpy.transpose(samples)

	polyfit = linear_fit.makePolyfit(xySamples)
	
	figure,plot = newPlot()
	# https://matplotlib.org/3.2.1/tutorials/text/mathtext.html
	plot.set_xlabel(r'Spannung $\mathit{U}$ [V]')
	plot.set_ylabel(r'Stromstärke $\mathit{I}$ [A]')

	addDefaultGridlines(plot)
	linear_fit.drawSamples(plot,xySamples)
	linear_fit.drawFit(plot,xySamples,polyfit)
	linear_fit.drawInfobox(plot,xySamples,polyfit)

	fileInfo = getFileinfo(path)
	figure.savefig('output/'+fileInfo['name']+'.png', dpi=300)

	# index += 1
	# if index > 4:
	# 	print('>>> limit loop during development')
	# 	break

