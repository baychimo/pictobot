#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import gettext


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

###############################################################################
# TRANSLATIONS                                                                #
###############################################################################
# Path to translations folder
path_locale = os.path.abspath(os.path.join(ROOT_DIR, 'locale'))
# Application name (for translations)
app_name = 'PictoBot'
# Default locale
default_locale = 'en_US'

t = gettext.translation(
    app_name,
    path_locale,
    languages=[default_locale]
)
_ = t.gettext

# Set language --- "TEMPORARY"
gettext.install(app_name, path_locale)

###############################################################################
# IMAGES                                                                      #
###############################################################################
# Default height / width
img_height = 1920
img_width = 1080
thumbs_height = 256
thumbs_width = 256
