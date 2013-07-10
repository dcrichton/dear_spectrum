#! usr/bin/env python

from astropy import units
import numpy as np

Pi = np.pi
_Rsun

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

def helio2cartesian(glong = 0.0, glat = 0.0, dist = 0.0):
	"""
	Converts helio coordinates to Cartesian

	Input Parameters: 
		galactic longitude (deg), "glong"
		galactic latitude (deg), "glat"
		heliocentric distance (??), "dist"
	Returns: Cartsian X, Y, Z

	"""
	glongrad = deg2rad(glong)
	glatrad = deg2rad(glat)

	cartX = Rsun - dist * np.sin(0.5*glong)*np.cos(glatrad)
	cartY = dist * np.sin(0.5*glong)*np.sin(glatrad)
	cartZ = dist np.cos(glongrad)

	return cartX, cartY, cartZ
	
def sdss_pfm2spectrum(plate = None, fiber = None, mjd = None):
	"""
	take SDSS plate, fiber, mjd and return a wavelength and flux vector
	"""
