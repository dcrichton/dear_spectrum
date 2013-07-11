from __future__ import division, print_function
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser

class SegueData(object):

    def __init__(self,data_filepath, columns = None):
        '''
        Read in SEGUE data.

        data_filepath: Location of data file.
        columns: Columns to retain. If None, keep all.
                 (Default: None)
        
        '''
        hdulist = fits.open(data_filepath, memmap=True)
        data_table = hdulist[1]

        self.data_dict = {}

        if columns is None:
            columns = hdulist.columns.names
        
        for col in columns:
            self.data_dict[col] = table.data[col]


    def cut_bad_data(self):
        '''
        Cut all data with SDSS -9999 flag.
        '''
        for i,(k,v) in enumerate(self.data_dict.items()):
            if i==0:
                good_inds = (v != -9999)
            else:
                good_inds = good_inds & (v != -9999)

        for k,v in self.data_dict:
            self.data_dict[k] = v[good_inds]

    def histogram_data(self, out_file, nbins = None,
                       ranges = None, labels = None):
        '''
        Plot histograms of good data columns.

        nbins: Number of bins in histograms
        ranges: Ranges of histograms
        labels: X labels of plot. If None, uses column
                names. (Default None)
        '''
        # fig, axes = plt.subplots(1,len(self.data_dict.keys()))
        
        # for ax,(k,v) in zip(axes,
        #                     self.data_dict.iteritems(),
        #                     bins,ranges):
        #     ax.hist(radial_velocity,bins=30)
            

        
	# axes[0].hist(radial_velocity,bins=30)
	# axes[0].set_xlabel("Radial Velocity")
	# axes[1].hist(heliocentric_distance,range=[0,100],bins=30)
	# axes[1].set_xlabel("Heliocentric Distance")
	# axes[2].hist(metallicity,bins=30)
	# axes[2].set_xlabel("FeH")
	# plt.tight_layout()
	# fig.savefig("block_1.pdf")
