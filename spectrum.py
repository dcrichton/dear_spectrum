"""
D.E.A.R team: Devin C., Ekta P., Alex G., Rachael A.
"""

from __future__ import division, print_function

__author__ = "rmalexan <rmalexan@pha.jhu.edu>"

# Standard libraries
import utils

class Spectrum(object):

	def __init__(self,wave=None,flux=None,err=None):
    	self.wave = wave
    	self.flux = flux
    	self.err = err