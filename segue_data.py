from __future__ import division, print_function
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser

class SegueData(object):
	"""
	other methods we want to write:
    
	from_dict -- create a new instance of SequeData given a dictionary instead of a file
	selection -- input a keyword and a cut on that keyword and return a new SequeData object
	                        with the same columns, but rows based on cut
	get_pfm -- return a list of plate,fiber,mjd tuples for every row in the SequeData object 
	                        (possible keyword-- selection)
	"""
	def __init__(self, data_filepath = None, data_dict = None,
                     columns = None, memmap = True, nrows = None):
		'''
		Read in SEGUE data. Must specify either data_filepath
                or data_dict.

		data_filepath: Location of data file.
		columns: Columns to retain. If None, keep all.
		         (Default: None)
		
		'''

                if (data_filepath is None) and not (data_dict is None):
                        self.data_dict = data_dict
                elif not (data_filepath is None):
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
                                if nrows is None:
                                        self.data_dict[col] = data_table.data[col]
                                else:
                                        self.data_dict[col] = data_table.data[col][:nrows]

        def iterrows(self):
                '''
                Returns an iterable the traverses through the stored rows
                and returns a dict of column:row_value for each row.
                '''
                cols = self.data_dict.keys()
                for i in range(len(self.data_dict[cols[0]])):
                        yield {c:self.data_dict[c][i] for c in cols}
                                        
        def select(self, column, selection_function = None):
                '''
                Return a SegueData data object which is the current object
                cut using a selection function operated on column. As well
                as the indices that were cut.

                column: Column to select with.
                selection_function: A function that returns true for
                values of the column that will be returned. If None
                return all rows in the column. (Default: None)
                '''
                if not column in self.data_dict.keys():
                        raise ValueError("Column does not exist.")

                if selection_function is None:
                        indices = np.ones(len(self.data_dict[column]),dtype=bool)
                else:
                        indices = selection_function(self.data_dict[column])
                new_dict = {}
                for col in self.data_dict.keys():
                        new_dict[col] = self.data_dict[col][indices]
                return SegueData(data_dict = new_dict), indices
                                                
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
                
    def get_cols(self,columns_to_return,column_to_select=None,selection_function = None):
   		"""	
    	get_cols -- return a list of columns requested as tuples for every row in the SequeData object 
	                        (possible keyword-- selection)
		"""
		for column in columns_to_return:
			if column not in self.data_dict.keys():
				raise KeyError("requested column does not exist in Seque_Data object")
		
		get_cols_dictionary = self.data_dict	
					
		if column_to_select:
			new_cols,indices = self.select(column_to_select,selection_function)
			get_cols_dictionary = new_cols.data_dict
		
		list_to_return = []	
		for row in get_cols_dictionary.iter_rows():
			my_tuple = ()
			for column in columns_to_return:
				my_tuple = my_tuple + (row[column],)
			list_to_return.append(my_tuple)
		return list_to_return
