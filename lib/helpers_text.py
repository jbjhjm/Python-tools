from math import floor, log10
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt

# format number to be shown as "1*10^x" instead of "1ex"
def sci_notation_tex(num, decimal_digits=1, precision=None, exponent=None):
    """
    Returns a string representation of the scientific
    notation of the given number formatted for use with
    LaTeX or Mathtext, with specified number of significant
    decimal digits and precision (number of decimal digits
    to show). The exponent to be used can also be specified
    explicitly.
    """
    if exponent is None:
        exponent = int(floor(log10(abs(num))))
    coeff = round(num / float(10**exponent), decimal_digits)
    if precision is None:
        precision = decimal_digits

    return r"${0:.{2}f}\cdot10^{{{1:d}}}$".format(coeff, exponent, precision)

def sci_notation_mathtext(x, fmt="%1.2e"):
	s = fmt % x
	decimal_point = '.'
	positive_sign = '+'
	multiplicator_sign = r'\times'
	multiplicator_sign = r'\cdot'
	tup = s.split('e')
	significand = tup[0].rstrip(decimal_point)
	sign = tup[1][0].replace(positive_sign, '')
	exponent = tup[1][1:].lstrip('0')
	
	if exponent:
		exponent = '10^{%s%s}' % (sign, exponent)

	if significand and exponent:
		s =  r'%s{%s}%s' % (significand, multiplicator_sign, exponent)
	else:
		s =  r'%s%s' % (significand, exponent)
	return "${}$".format(s)

# def sci_notation_mathtext(num):
# 	f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
# 	g = lambda x,pos : r"${}$".format(f._formatSciNotation('%1.10e' % x))
# 	fmt = mticker.FuncFormatter(g)
# 	return fmt(num).replace('×','*')