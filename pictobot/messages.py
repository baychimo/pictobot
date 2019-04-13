#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from settings.base import _

###############################################################################
# INFO MESSAGES                                                               #
###############################################################################
# Dict containing info messages, order does not matter
info_messages = {
    'QUERY_MSG': _('Please type your query'),
    'RESULTS_MSG': _('Showing result(s) for'),
    'NO_RESULT_MSG_1': _('Sorry. No match found for'),
    'NO_RESULT_MSG_2': _('\nMaybe you can try to /browse through the '
                         'pictograms instead...'),
    'SETTINGS_MSG': _('Welcome to the Machine.\n'
                      'Please enter root password: ****************\n\n'
                      '...thank you...\n\n'
                      '...processing...\n'
                      '...processing...\n'
                      '...processing...\n\n'
                      'Just kidding :-)\n'
                      'Language settings coming soon...'),
    'HELP_MSG': _('I can help you communicate via pictograms in the real '
                  'world.\n'
                  'When no one around you speaks your language(s), while '
                  'you are traveling abroad for example, just show what '
                  "you mean if you can't say it!\n\n"
                  "Either send me a query like 'Hotel' or 'Fast food', "
                  'or use one of these commands:\n'
                  '/browse - to browse through pictograms\n'
                  '/search - to find a pictogram\n\n'
                  'I work inline too:'),
    'SHARE_MSG': _('Send a pictogram to a friend'),
    'START_MSG': _('Hello!'),
    'START_INLINE_MSG': _('Hello, you seem to have a problem with inline '
                          'search. Not every concept is available at this '
                          "time, sorry if you can't find what you need"
                          '.\n\n'
                          "Try simple queries like 'Water' or 'Train'."),
    'SWITCH_PM_MSG': _("Sorry, nothing found. Tap for help"),
    'SWITCH_PM_PARAM': _('Water')
}

###############################################################################
# ERROR MESSAGES                                                              #
###############################################################################
# Dict containing error messages, order does not matter
error_messages = {
    'UNKNOWN_COMMAND': _('Sorry, I did not understand that command'),
    'UNKNOWN_TYPE_AUDIO': _('Sorry, I do not understand audio'),
    'UNKNOWN_TYPE_DOCUMENT': _('Sorry, I do not understand documents'),
    'UNKNOWN_TYPE_PHOTO': _('Sorry, I do not understand photos or images'),
    'UNKNOWN_TYPE_STICKER': _('Sorry, I do not understand stickers'),
    'UNKNOWN_TYPE_VIDEO': _('Sorry, I do not understand videos'),
    'UNKNOWN_TYPE_VOICE': _('Sorry, I do not understand voice messages'),
    'UNKNOWN_TYPE_CONTACT': _('Sorry, I do not understand contact '
                              'information'),
    'UNKNOWN_TYPE_LOCATION': _('Sorry, I do not understand location '
                               'information'),
    'UNKNOWN_TYPE_VENUE': _('Sorry, I do not understand venue '
                            'information'),
    'UNKNOWN_TYPE': _('Sorry, I do not understand this message'),
    'PICTO_NOT_FOUND':
        _('Sorry, there has been an error with this pictogram.'
          '\nMy Creator has been notified')
}
