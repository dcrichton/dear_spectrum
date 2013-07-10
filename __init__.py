#! usr/bin/env python

"""
D.E.A.R. team: Deven C., Ekta P., Alex G., Rachael A.
"""

from __future__ import division
import sys
import logging


# create logger
logger = logging.getLogger(__name__)

# define a handler to write log messages to stdout
sh = logging.StreamHandler(stream=sys.stdout)

# define the format for the log messages, here: "level name: message"
formatter = logging.Formatter("[%(levelname)s]: %(message)s")
sh.setFormatter(formatter)
logger.addHandler(sh)

