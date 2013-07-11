from __future__ import division, print_function
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser

class SegueData(object):

    def __init__(data_filepath, columns = None):
        '''
        Read in SEGUE data.

        data_filepath: Location of data file.
        columns: Columns to retain. If None, keep all.
                 (Default: None)
        
        '''
        pass

    def cut_bad_data():
        '''
        Cut all data with SDSS -9999 flag.
        '''
        pass

    def histogram_data(out_file, nbins = None, ranges = None, labels = None):
        '''
        Plot histograms of good data columns.

        nbins: Number of bins in histograms
        ranges: Ranges of histograms
        labels: X labels of plot. If None, uses column
                names. (Default None)
        '''
        pass
