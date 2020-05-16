
# see https://data36.com/linear-regression-in-python-numpy-polyfit/

import numpy
import pandas
import matplotlib
import matplotlib.pyplot as pyplot
from typing import Tuple
from .helpers_text import sci_notation_mathtext
from .helpers_plot import addTextBox, drawSamples, newPlot
from sklearn.metrics import mean_squared_error


# TODO: Typing
def makePolyfit(samples:numpy.ndarray):
	# cov is covariance matrix
	model,cov = numpy.polyfit(samples[0], samples[1], 1, cov=True)
	yfit = numpy.polyval(model,samples[0])

	# calculate y values using the model
	predict = numpy.poly1d(model)

	deviation = yfit - samples[1]
	sigma = numpy.std( deviation )

	# calculate the uncertainty by squaring the diagonal of covariance matrix.
	uncertainty = numpy.sqrt(numpy.diag(cov))

	return {
		'model':model,
		'cov':cov,
		'deviation':deviation,
		'sigma':sigma,
		'uncertainty':uncertainty
	}


def drawFit(plot:matplotlib.axes.SubplotBase, samples:numpy.ndarray, polyfit):
	# plot options https://matplotlib.org/tutorials/introductory/pyplot.html
	# plot linear graph between min and max sample values
	predict = numpy.poly1d(polyfit['model'])
	linear_x = [min(samples[0]), max(samples[0])]
	linear_y = predict(linear_x)
	plot.plot(linear_x, linear_y, color = 'red', zorder=2)



def drawDeviation(plot:matplotlib.axes.SubplotBase, samples:numpy.ndarray, polyfit):
	plot.plot(samples[0], polyfit['deviation'], zorder=1, color='#bbf', linewidth=1)



def drawInfobox(plot:matplotlib.axes.SubplotBase, samples:numpy.ndarray, polyfit):
	# https://thepythonguru.com/python-string-formatting/
	# https://pyformat.info/
	# {{{}}} -- see https://stackoverflow.com/questions/53781815/superscript-format-in-matplotlib-plot-legend
	textstr = '\n'.join((
		r'a = {}'.format(sci_notation_mathtext(polyfit['model'][0])),
		r'b = {}'.format(sci_notation_mathtext(polyfit['model'][1])),
		r'Cov [a] = {}'.format(sci_notation_mathtext(polyfit['uncertainty'][0])),
		r'Cov [b] = {}'.format(sci_notation_mathtext(polyfit['uncertainty'][1])),
		r'$\sigma$ = {}'.format(sci_notation_mathtext(polyfit['sigma'])),
	))

	addTextBox(plot,textstr)

