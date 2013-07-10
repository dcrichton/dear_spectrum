"""
D.E.A.R team: Devin C., Ekta P., Alex G., Rachael A.
"""

from __future__ import division, print_function

__author__ = "rmalexan <rmalexan@pha.jhu.edu>"

# Standard libraries
import utils

class Star(object):
    
    def __init__(self, radial_velocity=None, metallicity=None, heliocentric_distance=None, galactic_longitude=None,galactic_latitude=None,galactocentric_distance=None):
        self.radial_velocity = radial_velocity
        self.metallicity = metallicity
        self.heliocentric_distance = heliocentric_distance
        self.galactic_longitude = galactic_longitude
        self.galactic_latitude = galactic_latitude
        self.galactocentric_distance = galactocentric_distance
        
        @property
        def galactocentric_distance(self):
        	if self == None:
        		galactocentric_distance = utils.helio2cartesian(glong=galactic_longitude,glat=galactic_latitude,dist=heliocentric_distance)
        	return galactocentric_distance
    
    