#!/usr/bin/env python 
"""
Script using DFI tools to calculate average dataframe. 

./avgdfi.py title parm1 parm2 
e.g. ./avgdfi.py 1fsa pctdfi pctfdfi 
"""

if __name__ == __main__ and len(sys.argv) > 2:
	#run code
	import dfitools as dfit
	pdbid = sys.argv[1]
	for parm in sys.argv[2:]:
		dfit.calc_avg(pdbid,parm)
else:
	print __doc__