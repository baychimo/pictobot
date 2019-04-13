#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .base import *

###############################################################################
# GLOBALS / DATA / PARAMETERS                                                 #
# We use dicts / ordered dicts to store static data and parameters            #
# If it gets too big or problematic, we'll switch to a database. In the       #
# meantime, we'll take every bit of performance we can get                    #
###############################################################################

ENV = 'production'
# Production (@YourProdBot)
TOKEN = '123456789:abcdef123456abcdef123456abcdef12345'

path_img = '/var/www/static.yourserver.com/pictobot/fullsize/'
path_thumbs = '/var/www/static.yourserver.com/pictobot/thumbs/'
external_path_img = 'https://static.yourserver.com/pictobot/fullsize/'
external_path_thumbs = 'https://static.yourserver.com/pictobot/thumbs/'

HOST = 'apps.yourserver.com/pictobot'
PORT = 5000
STATIC = 'static.yourserver.com/pictobot'
