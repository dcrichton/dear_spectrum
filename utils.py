#! usr/bin/env python

from __future__ import print_function, division

from astropy import units
import numpy as np
import astropy.units as u
import json
import urllib2

Pi = np.pi

def deg2rad(deg):
	"""
	Converts from degrees (input) to radians (output)
	"""
	return deg*Pi/180.0

def rad2deg(rad):
	"""
	Converts from radians (input) to degrees (output)
	"""
	return rad*180.0/Pi

def return_keys(dictionary):
    	print(dictionary.keys())
    	return dictionary.keys()

def helio2cartesian(glong = 0.0*u.deg, glat = 0.0*u.deg, dist = 0.0* u.parsec):
	"""
	Converts helio coordinates to Cartesian

	Input Parameters: 
		galactic longitude (deg), "glong"
		galactic latitude (deg), "glat"
		heliocentric distance (??), "dist"
	Returns: Cartsian X, Y, Z

	"""
		#u1, u2, u3 = glong.unit, glat.unit, dist.unit
	if not hasattr(glong, 'unit') & hasattr(glat, 'unit') & hasattr(dist, 'unit'):
		raise AttributeError('Input parameters must be Quantity-like objects')

	# Distance from the sun to the galactic center?
	_R0 = 8.0*u.kiloparsec

	cartX = (dist * np.sin(0.5*glong.to(u.rad).value)* 
                 np.cos((glat+180*u.deg).to(u.rad).value) - _R0)
	cartY = dist * np.sin(0.5*glong.to(u.rad).value)*np.sin(glat.to(u.rad).value)
	cartZ = dist * np.cos(glong.to(u.rad))

	return cartX, cartY, cartZ
	
def sdss_pfm2spectrum(plate = None, fiber = None, mjd = None):
	"""
	takes SDSS plate, fiber, mjd and returns a spectrum dictionary
	"""
	sdss_api_url = "http://api.sdss3.org/spectrum?plate={0}\&mjd={1}&fiber={2}&format=json".format(str(plate), str(fiber), str(mjd))
	response = urllib2.urlopen(sdss_api_url)

	# parse the returned JSON object into a Python dictionary
	spectrum = json.load(response) 
	""" 
	'http://api.sdss3.org/api_spectrum.html' :  An available option is to have the
	spectrum and its metadata returned as a JSON dictionary. Each spectrum returned
	is an entry in the dictionary with the spectrum unique id as the key and the
	value as another dictionary. The values of this dictionary contain both scalar
	values and arrays. Some of the more useful keys: 

	ra
	dec
	flux
	wavelengths
	z
	mjd
	run
	rerun
	camcol
	field

	"""

	return spectrum
