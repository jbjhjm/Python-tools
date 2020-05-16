import matplotlib
import numpy
import matplotlib.pyplot as pyplot
from typing import Tuple
#from typing import Literal


def addDefaultGridlines(plot:matplotlib.axes.SubplotBase):

	plot.xaxis.grid(True, which='major')
	plot.xaxis.grid(True, which='minor')
	plot.yaxis.grid(True, which='major')
	plot.yaxis.grid(True, which='minor')

	plot.axhline(y=0, color='#000', linewidth=1)
	plot.axvline(x=0, color='#000', linewidth=1)


# TODO: current anaconda ships with python 3.7 which does not support Literal.
# when available, update to "position:Literal['topright','bottomright']='bottomright'""
def addTextBox(plot:matplotlib.axes.SubplotBase, text:str, position='bottomright'):

	# these are matplotlib.patch.Patch properties
	props = dict(boxstyle='square', facecolor='#fff', alpha=1)

	# place a text box in upper left in axes coords
	# top right: xy=(1, 1), xytext=(15, 15), verticalalignment='top'
	# bottom right: xy=(1, 0), xytext=(-15, 15), verticalalignment='bottom'

	if position=='topright': positionArgs = {'xy':(1, 1), 'xytext':(15, 15), 'verticalalignment':'top', 'horizontalalignment':'right'}
	if position=='bottomright': positionArgs = {'xy':(1, 0), 'xytext':(-15, 15), 'verticalalignment':'bottom', 'horizontalalignment':'right'}

	plot.annotate(text, fontsize=10, bbox=props, zorder=10, xycoords='axes fraction', textcoords='offset points', **positionArgs )


def newPlot(existingFigure=False) -> Tuple[pyplot.figure, matplotlib.axes.SubplotBase]:
	if existingFigure: figure = existingFigure
	else: figure = pyplot.figure()

	plot = figure.add_subplot(1,1,1)
	return (figure,plot)


def drawSamples(plot:matplotlib.axes.SubplotBase, samples:numpy.ndarray):
	plot.scatter(samples[0],samples[1], c="#4444ff", s=1, zorder=5)
