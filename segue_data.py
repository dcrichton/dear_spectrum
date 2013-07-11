from __future__ import division, print_function
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser

class SegueData(object):

    def __init__(self,data_filepath, columns = None, memmap = True):
        '''
        Read in SEGUE data.

        data_filepath: Location of data file.
        columns: Columns to retain. If None, keep all.
                 (Default: None)
        
        '''
        hdulist = fits.open(data_filepath, memmap = memmap)
        data_table = hdulist[1]

        #find spectral types
	all_spec_types = set(data_table.data['SPECTYPE_HAMMER'])
	print("Spectral Types: ")
	print(all_spec_types)

        self.data_dict = {}

        if columns is None:
            columns = hdulist.columns.names
        
        for col in columns:
            self.data_dict[col] = data_table.data[col]


    def cut_bad_data(self):
        '''
        Cut all data with SDSS -9999 flag.
        '''
        for i,(k,v) in enumerate(self.data_dict.items()):
            if i==0:
                good_inds = (v != -9999)
            else:
                good_inds = good_inds & (v != -9999)

        for k,v in self.data_dict.items():
            self.data_dict[k] = v[good_inds]

    def histogram_data(self, out_file):#, nbins = None,
                       #ranges = None, labels = None):
        '''
        Plot histograms of good data columns.

        nbins: Number of bins in histograms
        ranges: Ranges of histograms
        labels: X labels of plot. If None, uses column
                names. (Default None)
        '''

        fig, axes = plt.subplots(1,len(self.data_dict.keys()))

        for i,(key,value) in enumerate(self.data_dict.items()):
            axes[i].hist(value)
            axes[i].set_xlabel(key.replace('_', ' '))
            
	plt.tight_layout()
	fig.savefig(out_file)
