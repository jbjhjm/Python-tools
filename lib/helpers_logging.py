# use pp.pprint to print formatted data in console
import pprint
pp = pprint.PrettyPrinter(indent=4)

def prettyPrint(*args):
	pp.pprint(*args)