
# Use LaTeX as text renderer to get text in true LaTeX
# If the two following lines are left out, Mathtext will be used
def enableLatex():
	import matplotlib as mpl
	mpl.rc('text', usetex=True)
