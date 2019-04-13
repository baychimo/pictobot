#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../pictobot')))

from pictobot import (
    core,
    keyboards,
    messages,
    pictograms
)
from pictobot.settings import local as local_settings
