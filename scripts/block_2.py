from __future__ import division, print_function
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser
from segue_data import SegueData
from utils import helio2cartesian
import astropy.units as u

if __name__ == '__main__':

	parser = ArgumentParser(description="Histogram plot attribues.")

	parser.add_argument("data_filepath", type=str,
                        help = "The location of the data file.")

	args = parser.parse_args()

        stars_data=SegueData(args.data_filepath, columns=['RV_ADOP','DIST_ADOP','FEH_ADOP','L','B'],
			     memmap = True, nrows = 10000)

	stars_data.cut_bad_data()

	GCENT, Z = [], []
	for glong, glat, dist in zip(stars_data.data_dict['L'],
	                             stars_data.data_dict['B'],
	                             stars_data.data_dict['DIST_ADOP']):
		glong = u.deg*glong
		glat = u.deg*glat
		dist = u.kiloparsec*dist
		x,y,z = helio2cartesian(glong,glat,dist)
		Z.append(z)
		print(len(Z),len(stars_data.data_dict['L']))
		GCENT.append((x**2+y**2+z**2)**.5)

	stars_data.data_dict['GCENT_DIST'] = GCENT
	stars_data.data_dict.pop('L')
	stars_data.data_dict.pop('B')
	stars_data.data_dict.pop('DIST_ADOP')

	stars_data.histogram_data('block_2.pdf')
