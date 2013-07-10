"""
D.E.A.R team: Devin C., Ekta P., Alex G., Rachael A.
"""

from __future__ import division, print_function

__author__ = "rmalexan <rmalexan@pha.jhu.edu>"

# Standard library

class Star(object):
    
    def __init__(self, radial_velocity=None, metallicity=None, heliocentric_distance=None):
        self.radial_velocity = radial_velocity
        self.metallicity = metallicity
        self.heliocentric_distance = heliocentric_distance
    
    