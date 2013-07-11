"""
D.E.A.R team: Devin C., Ekta P., Alex G., Rachael A.
"""

from __future__ import division, print_function

__author__ = "rmalexan <rmalexan@pha.jhu.edu>"

# Standard libraries
import utils

class Spectrum(object):

	"""
	Spectrum expects a single spectrum dictionary
    Can be taken directly from SDSSS API (api.sdss3.org)
    can also provide an sdss tuple and pull directly from the API
    
    methods:
    show_keys returns dictionary keywords of spectrum
    
    interpolate_spectra takes another spectrum object and returns the
    flux on the wavelength scale of the self spectrum
    
    coadd takes a list of spectrum objects and returns the self wavelength list
    and the normalized, coadded flux list
    
	"""

	def __init__(self,spectrum = dict(), sdss=None):
    	if sdss:
    		"""
    		sdss must be a tuple of plate, fiber, mjd
    		"""
    		plate,fiber,mjd = sdss
    		spectrum = sdss_pfm2spectrum(plate = plate,fiber = fiber, mjd = mjd)
    	self.spectrum = spectrum
    	
    def show_keys(self):
    	return_keys(self.spectrum)
    
    def interpolate_spectra(self,other_spectrum):
    	wavelength_interpolation = interpolate.interp1d(other_spectrum['wavelengths'], 
    														other_spectrum['flux'],kind='cubic',bounds_error = False)
    	return wavelength_interpolation(self.spectrum['wavelengths'])	
    
    def coadd(self,additional_spectra):
    	from scipy import interpolate
    	"""
    	Take another spectrum object (or list of spectrum objects), interpolate the two to the same
    	wavelength grid, and coadd
    	"""
    	# in future implement spline instead of cubic 
    	flux_total = self.spectrum['flux']
    	for other_spectrum in additional_spectra:
			flux_total += interpolate_spectra(other_spectrum)										
    	return self.spectrum['wavelengths'], flux_total/(len(additional_spectra) +1)
    	#in future: add inverse variance weighting for coadd
    	
    	
    	