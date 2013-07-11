from __future__ import division, print_function
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser
from segue_data import SegueData

if __name__ == '__main__':

	parser = ArgumentParser(description="Histogram plot attribues.")

	parser.add_argument("data_filepath", type=str,
                        help = "The location of the data file.")

	args = parser.parse_args()

	# data = ds.utils.parse_data(data_filepath = args.data_filepath,
	#                            columns = ['RV_ADOP','FEH_ADOP','DIST_ADOP'])
    
	#opens fits file
	stars_data=SegueData(args.data_filepath, columns=['RV_ADOP','DIST_ADOP','FEH_ADOP'],
			     memmap=False)

	#find only good data (delete all -9999 values)
 	stars_data.cut_bad_data()

	#plot
	stars_data.histogram_data('block_1.pdf')#, nbins=30, ranges=[0,100])
	

    


