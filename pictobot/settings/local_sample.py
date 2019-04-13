#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .base import *

###############################################################################
# GLOBALS / DATA / PARAMETERS                                                 #
# We use dicts / ordered dicts to store static data and parameters            #
# If it gets too big or problematic, we'll switch to a database. In the       #
# meantime, we'll take every bit of performance we can get                    #
###############################################################################

ENV = 'local'
# Test (@YourTestBot)
TOKEN = '123456789:abcdef123456abcdef123456abcdef12345'

# Userbot
api_id = 535397
api_hash = 'cdef123456abcdef123456abcdef1234'

path_img = ROOT_DIR + '/images/full/'
path_thumbs = ROOT_DIR + '/images/thumbs/'
external_path_img = ''     # Only for testing, however must be set in production
external_path_thumbs = ''  # Only for testing, however must be set in production
