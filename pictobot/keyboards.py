#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from settings.base import _
from pictograms import *
from collections import OrderedDict

###############################################################################
# INLINE KEYBOARDS                                                            #
# Inception of dicts containing keyboard parameters.                          #
# Order does not matter here, apart for the layouts inner dicts               #
###############################################################################
keyboards = {
    # Dict describing main inline keyboard : categories of pictograms
    'KB_MAIN': {
        'layout': OrderedDict([
            (_('Emergency') + ' / ' + _('Health'), 'KB_EMERGENCY'),
            (_('Food') + ' / ' + _('Water'), 'KB_FOOD_WATER'),
            (_('Hygiene') + ' / ' + _('Sanitation'), 'KB_HYGIENE'),
            (_('Transport'), 'KB_TRANSPORT'),
            (_('Accommodation'), 'KB_ACCOMMODATION'),
            (_('Useful Services'), 'KB_USEFUL_SERVICES'),
            (_('More') + ' >>', 'KB_MORE')
        ]),
        'text': _('Select category')
    },
    # Dict describing 2nd level keyboard : food / water category
    'KB_FOOD_WATER': {
        'layout': OrderedDict([
            (pictograms['DRINKING_WATER']['title'], 'DRINKING_WATER'),
            (pictograms['MARKET']['title'], 'MARKET'),
            (pictograms['SUPERMARKET']['title'], 'SUPERMARKET'),
            (pictograms['RESTAURANT']['title'], 'RESTAURANT'),
            (pictograms['FOOD']['title'], 'FOOD'),
            (_('More') + ' >>', 'KB_FOOD_WATER_2'),
            ('<< ' + _('Back'), 'KB_MAIN')
        ]),
        'text': _('Category') + ' :: ' + _('Food') + ' / ' + _('Water')
    },
    # Dict describing 3rd level keyboard : food / water category
    'KB_FOOD_WATER_2': {
        'layout': OrderedDict([
            (pictograms['WATER_BOTTLE']['title'], 'WATER_BOTTLE'),
            (pictograms['FAST_FOOD']['title'], 'FAST_FOOD'),
            (pictograms['BAR']['title'], 'BAR'),
            (pictograms['COFFEE']['title'], 'COFFEE'),
            ('<< ' + _('Back'), 'KB_FOOD_WATER')
        ]),
        'text': _('Category') + ' :: ' +
        _('Food') + ' / ' + _('Water') + ' [2]'
    },
    # Dict describing 2nd level keyboard : emergency / health category
    'KB_EMERGENCY': {
        'layout': OrderedDict([
            (pictograms['FIRST_AID']['title'], 'FIRST_AID'),
            (pictograms['AMBULANCE']['title'], 'AMBULANCE'),
            (pictograms['DOCTOR']['title'], 'DOCTOR'),
            (pictograms['HOSPITAL']['title'], 'HOSPITAL'),
            (pictograms['POLICE']['title'], 'POLICE'),
            (_('More') + ' >>', 'KB_EMERGENCY_2'),
            ('<< ' + _('Back'), 'KB_MAIN')
        ]),
        'text': _('Category') + ' :: ' + _('Emergency') + ' / ' + _('Health')
    },
    # Dict describing 3rd level keyboard : emergency / health category
    'KB_EMERGENCY_2': {
        'layout': OrderedDict([
            (pictograms['DENTIST']['title'], 'DENTIST'),
            (pictograms['MEDICINE']['title'], 'MEDICINE'),
            (pictograms['BAND_AID']['title'], 'BAND_AID'),
            (pictograms['SHELTER']['title'], 'SHELTER'),
            ('<< ' + _('Back'), 'KB_EMERGENCY')
        ]),
        'text': _('Category') + ' :: ' + _('Emergency') + ' / ' + _('Health') +
        ' [2]'
    },
    # Dict describing 2nd level keyboard : hygiene / sanitation category
    'KB_HYGIENE': {
        'layout': OrderedDict([
            (pictograms['TOILETS']['title'], 'TOILETS'),
            (pictograms['SHOWER']['title'], 'SHOWER'),
            (pictograms['SOAP']['title'], 'SOAP'),
            (pictograms['TOILET_PAPER']['title'], 'TOILET_PAPER'),
            (pictograms['WASHING_MACHINE']['title'], 'WASHING_MACHINE'),
            ('<< ' + _('Back'), 'KB_MAIN')
        ]),
        'text': _('Category') + ' :: ' + _('Hygiene') + ' / ' + _('Sanitation')
    },
    # Dict describing 2nd level keyboard : transport category
    'KB_TRANSPORT': {
        'layout': OrderedDict([
            (pictograms['TAXI']['title'], 'TAXI'),
            (pictograms['BUS']['title'], 'BUS'),
            (pictograms['TRAIN']['title'], 'TRAIN'),
            (pictograms['CAR_RENTAL']['title'], 'CAR_RENTAL'),
            (pictograms['AIRPLANE']['title'], 'AIRPLANE'),
            (_('More') + ' >>', 'KB_TRANSPORT_2'),
            ('<< ' + _('Back'), 'KB_MAIN')
        ]),
        'text': _('Category') + ' :: ' + _('Transport')
    },
    # Dict describing 3rd level keyboard : transport category
    'KB_TRANSPORT_2': {
        'layout': OrderedDict([
            (pictograms['GROUND_TRANSPORTATION']['title'],
                'GROUND_TRANSPORTATION'
             ),
            (pictograms['FERRY_BOAT']['title'], 'FERRY_BOAT'),
            (pictograms['SAIL_BOAT']['title'], 'SAIL_BOAT'),
            (pictograms['VAN']['title'], 'VAN'),
            (pictograms['MOTORBIKE']['title'], 'MOTORBIKE'),
            ('<< ' + _('Back'), 'KB_TRANSPORT')
        ]),
        'text': _('Category') + ' :: ' + _('Transport') + ' [2]'
    },
    # Dict describing 2nd level keyboard : accommodation category
    'KB_ACCOMMODATION': {
        'layout': OrderedDict([
            (pictograms['HOTEL']['title'], 'HOTEL'),
            (pictograms['HOSTEL']['title'], 'HOSTEL'),
            (pictograms['CAMPING']['title'], 'CAMPING'),
            (pictograms['ROOM_SERVICE']['title'], 'ROOM_SERVICE'),
            ('<< ' + _('Back'), 'KB_MAIN')
        ]),
        'text': _('Category') + ' :: ' + _('Accommodation')
    },
    # Dict describing 2nd level keyboard : useful services category
    'KB_USEFUL_SERVICES': {
        'layout': OrderedDict([
            (pictograms['ATM']['title'], 'ATM'),
            (pictograms['BANK']['title'], 'BANK'),
            (pictograms['JUSTICE']['title'], 'JUSTICE'),
            (pictograms['HAIRDRESSER']['title'], 'HAIRDRESSER'),
            (pictograms['GAS_STATION']['title'], 'GAS_STATION'),
            (_('More') + ' >>', 'KB_USEFUL_SERVICES_2'),
            ('<< ' + _('Back'), 'KB_MAIN')
        ]),
        'text': _('Category') + ' :: ' + _('Useful Services')
    },
    # Dict describing 3rd level keyboard : useful services category
    'KB_USEFUL_SERVICES_2': {
        'layout': OrderedDict([
            (pictograms['PHOTOGRAPHER']['title'], 'PHOTOGRAPHER'),
            (pictograms['MUSEUM']['title'], 'MUSEUM'),
            (pictograms['INTERNET_ACCESS']['title'], 'INTERNET_ACCESS'),
            ('<< ' + _('Back'), 'KB_USEFUL_SERVICES')
        ]),
        'text': _('Category') + ' :: ' + _('Useful Services') + ' [2]'
    },
    # Dict describing 2nd level keyboard : other / more category
    'KB_MORE': {
        'layout': OrderedDict([
            (_('Useful Items'), 'KB_USEFUL_ITEMS'),
            (_('Nature'), 'KB_NATURE'),
            (_('Sports'), 'KB_SPORTS'),
            (_('Religion'), 'KB_RELIGION'),
            (_('Alien contact'), 'KB_ALIEN'),
            ('<< ' + _('Back'), 'KB_MAIN')
        ]),
        'text': _('Select category')
    },
    # Dict describing 3rd level keyboard : useful items category
    'KB_USEFUL_ITEMS': {
        'layout': OrderedDict([
            (pictograms['ADAPTER_PLUG']['title'], 'ADAPTER_PLUG'),
            (pictograms['CHARGER']['title'], 'CHARGER'),
            (pictograms['SUNGLASSES']['title'], 'SUNGLASSES'),
            (pictograms['BEACH_UMBRELLA']['title'], 'BEACH_UMBRELLA'),
            (pictograms['TOOLS']['title'], 'TOOLS'),
            (_('More') + ' >>', 'KB_USEFUL_ITEMS_2'),
            ('<< ' + _('Back'), 'KB_MORE')
        ]),
        'text': _('Category') + ' :: ' + _('Useful Items')
    },
    # Dict describing 4th level keyboard : useful items category
    'KB_USEFUL_ITEMS_2': {
        'layout': OrderedDict([
            (pictograms['HAMMER']['title'], 'HAMMER'),
            (pictograms['SCREWDRIVER']['title'], 'SCREWDRIVER'),
            (pictograms['WRENCH']['title'], 'WRENCH'),
            (pictograms['UMBRELLA']['title'], 'UMBRELLA'),
            (pictograms['PENCIL']['title'], 'PENCIL'),
            ('<< ' + _('Back'), 'KB_USEFUL_ITEMS')
        ]),
        'text': _('Category') + ' :: ' + _('Useful Items') + ' [2]'
    },
    # Dict describing 3rd level keyboard : nature category
    'KB_NATURE': {
        'layout': OrderedDict([
            (pictograms['PARK']['title'], 'PARK'),
            (pictograms['BEACH']['title'], 'BEACH'),
            (pictograms['LAKE']['title'], 'LAKE'),
            (pictograms['OCEAN']['title'], 'OCEAN'),
            ('<< ' + _('Back'), 'KB_MORE')
        ]),
        'text': _('Category') + ' :: ' + _('Nature')
    },
    # Dict describing 3rd level keyboard : sports category
    'KB_SPORTS': {
        'layout': OrderedDict([
            (pictograms['HIKE']['title'], 'HIKE'),
            (pictograms['CYCLING']['title'], 'CYCLING'),
            (pictograms['SKYDIVING']['title'], 'SKYDIVING'),
            (pictograms['SCUBA_DIVING']['title'], 'SCUBA_DIVING'),
            (pictograms['SWIMMING']['title'], 'SWIMMING'),
            (pictograms['INDOOR_SWIMMING']['title'], 'INDOOR_SWIMMING'),
            ('<< ' + _('Back'), 'KB_MORE')
        ]),
        'text': _('Category') + ' :: ' + _('Sports')
    },
    # Dict describing 3rd level keyboard : religion category
    'KB_RELIGION': {
        'layout': OrderedDict([
            (pictograms['CHURCH']['title'], 'CHURCH'),
            (pictograms['MOSQUE']['title'], 'MOSQUE'),
            (pictograms['HINDU_TEMPLE']['title'], 'HINDU_TEMPLE'),
            (pictograms['BUDDHIST_TEMPLE']['title'], 'BUDDHIST_TEMPLE'),
            (pictograms['SYNAGOGUE']['title'], 'SYNAGOGUE'),
            (pictograms['CHAPEL']['title'], 'CHAPEL'),
            ('<< ' + _('Back'), 'KB_MORE')
        ]),
        'text': _('Category') + ' :: ' + _('Religion')
    },
    # Dict describing 3rd level keyboard : alien contact category
    'KB_ALIEN': {
        'layout': OrderedDict([
            (pictograms['TRIANGLE']['title'], 'TRIANGLE'),
            (pictograms['BORG']['title'], 'BORG'),
            ('<< ' + _('Back'), 'KB_MORE')
        ]),
        'text': _('Category') + ' :: ' + _('Alien contact')
    }
}
