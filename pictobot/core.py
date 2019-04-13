#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pictobot is a `Telegram <https://www.telegram.org/>`_ Bot, that is, a
`conversational program <https://en.wikipedia.org/wiki/Chatterbot>`_.
It is designed to help you communicate while you are traveling abroad.
"""
import logging
from collections import OrderedDict
from uuid import uuid4
from fuzzywuzzy import (
    fuzz,
    process
)
from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto
)
from telegram.ext import (
    CallbackQueryHandler,
    InlineQueryHandler,
    CommandHandler,
    MessageHandler,
    Filters,
    Updater
)

# Run with production settings:
# from settings.production import *

# Run with dev/test settings:
from settings.local import *

# Loads of import * here, these are just dicts being loaded (where the data is
# stored)
from pictograms import *
from keyboards import *
from messages import *
from search import *


###############################################################################
# LOGGING                                                                     #
###############################################################################
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    # level=logging.DEBUG
    level=logging.INFO
)
logger = logging.getLogger(__name__)


###############################################################################
# START                                                                       #
###############################################################################
def start(bot, update, args):
    """/start command. Displays welcome message.

    Displays a welcome message and a help message (via a triggered /help
    command). If the user is sent here after an unsuccessful inline search a
    hopefully helpful message is shown.

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
        args(tuple): search terms.
    """
    switch_pm_parameter = ' '.join(args)
    # /start does not take args, unless WE give them. The only valid case is
    # when an inline_search does not yield any result (not found)
    if switch_pm_parameter == info_messages['SWITCH_PM_PARAM']:
        reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text='Try ' + " '" + switch_pm_parameter + "'",
                switch_inline_query=switch_pm_parameter
            )
        ]])
        bot.sendMessage(
            chat_id=update.message.chat_id,
            text=info_messages['START_INLINE_MSG'],
            reply_markup=reply_markup
        )
    else:
        bot.sendMessage(
            chat_id=update.message.chat_id,
            text=info_messages['START_MSG']
        )
        help(bot, update)


###############################################################################
# HELP                                                                        #
###############################################################################
def help(bot, update):
    """/help command. Displays help message to the user.

    The user either used the /help command or is being sent here after getting
    lost. A helpful message is displayed, and a reminder button that the
    inline query mode is available.

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
    """
    reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text=info_messages['SHARE_MSG'],
            switch_inline_query=''
        )
    ]])
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=info_messages['HELP_MSG'],
        reply_markup=reply_markup
    )


###############################################################################
# SETTINGS                                                                    #
###############################################################################
def settings(bot, update):
    """/settings command. Not implemented yet. Not advertised to BotFather
    either.

    Displays a joke message if anyone ever tries this command until it's
    implemented.

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
    """
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=info_messages['SETTINGS_MSG']
    )


###############################################################################
# SEARCH                                                                      #
###############################################################################
# 4 possible paths to start a search :
# N°1 :: user types his/her query directly (no command) -> quick_search
# N°2 & 3 :: /search command is used -> cmd_search
# N°4 :: inline search is used

def quick_search(bot, update):
    """User types his/her query directly (no command)

    User being rerouted to classic search function, it's just a wrapper really.

    Args:
        bot: (object) the bot instance.
        update: (object) the message sent by the user.
    """
    raw_query = update.message.text
    # Impossible ?
    if not raw_query:
        return
    else:
        search(bot, update, raw_query)


def cmd_search(bot, update, args):
    """**_/search_** command

    User typed /search command. Either with some search query behind it. Or
    without any text, in which case we ask her/him to type his/her query.

    Args:
        bot: (object) the bot instance.
        update: (object) the message sent by the user.
        args: (list) search query typed by the user.
    """
    raw_query = ' '.join(args)
    if not raw_query:
        # User typed /search command without any text (args empty)
        bot.sendMessage(
            chat_id=update.message.chat_id,
            text=info_messages['QUERY_MSG']
        )
    else:
        search(bot, update, raw_query)


def search(bot, update, raw_query):
    """Search function

    Clean up the search query via sanitize_string function, get results from
    fuzzy_search function. Either return results as a keyboard or display a
    "not found" message.

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
        raw_query(list): search query typed by the user.
    """
    # Sanitize / clean up search query for better search results
    query = sanitize_string(raw_query)
    results = fuzzy_search(query, 7)
    if results:
        # Build keyboard from search results
        kb_results = OrderedDict([(i[0], i[1]) for i in results])
        reply_markup = build_keyboard(kb_results)
        # Send search results as an inline keyboard
        bot.sendMessage(
            chat_id=update.message.chat_id,
            text=info_messages['RESULTS_MSG'] + " '" + raw_query + "'",
            reply_markup=reply_markup
        )
    else:
        bot.sendMessage(
            chat_id=update.message.chat_id,
            text=info_messages['NO_RESULT_MSG_1'] +
            " '" + raw_query + "' " +
            info_messages['NO_RESULT_MSG_2']
        )


def inline_search(bot, update):
    """Inline search function: called everytime the user types a character.

    This type of search is only functionning when the image folders are on a
    web server, Telegram expects proper URLs.

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
    """
    raw_query = update.inline_query.query
    inline_results = []
    switch_pm_text = None
    switch_pm_parameter = None
    # While waiting for the user to type, we show the 14 most common pictograms.
    if not raw_query:
        for result in default_search_results:
            inline_results.append(
                InlineQueryResultPhoto(
                    id=uuid4(),
                    title=pictograms[result]['title'],
                    photo_url=external_path_img +
                    pictograms[result]['filename'],
                    thumb_url=external_path_thumbs +
                    pictograms[result]['filename'],
                    photo_width=img_width,
                    photo_height=img_height
                )
            )
    else:
        # While the user types and until he is done or nothing is found,
        # we search for every update (quite consuming, but hey).
        query = sanitize_string(raw_query)
        results = fuzzy_search(query, 7)
        if results:
            for result in results:
                inline_results.append(
                    InlineQueryResultPhoto(
                        id=uuid4(),
                        title=result[0],
                        photo_url=external_path_img +
                        pictograms[result[1]]['filename'],
                        thumb_url=external_path_thumbs +
                        pictograms[result[1]]['filename'],
                        photo_width=img_width,
                        photo_height=img_height
                    )
                )
        else:
            switch_pm_text = info_messages['SWITCH_PM_MSG']
            switch_pm_parameter = info_messages['SWITCH_PM_PARAM']
    bot.answerInlineQuery(
        inline_query_id=update.inline_query.id,
        results=inline_results,
        switch_pm_text=switch_pm_text,
        switch_pm_parameter=switch_pm_parameter
    )


def sanitize_string(query):
    """Clean up user input

    Remove unwanted characters from strings and convert uppercase caharacters
    before search: for better scores on Levenshtein distances.

    Args:
        query(string): the user's search strings.

    Returns:
        string: A sanitized string.
    """
    # 1st pass we remove non alphanumeric characters (emojis, slashes, etc.)
    first_pass = ''.join(c for c in query if c.isalnum() or c == ' ')
    # 2nd pass we remove multiple spaces for better fuzzy matching score
    second_pass = ' '.join(first_pass.split())
    # 3rd pass we convert to lowercase for better fuzzy matching score
    third_pass = second_pass.lower()
    return third_pass


def fuzzy_search(query, limit=7):
    """Fuzzy search the dict containing the search keywords

    Return best results sorted by score, descending.

    Args:
        query(string): the user's search strings.
        limit(int): number of results to return.

    Returns:
        list: A list of results sorted by score and simple_ratio(fuzz.ratio)
    """
    results = []
    # Create list of tuples of results (of the form (title, key, score), where
    # key is a pictogram
    for key in pictograms:
        score = process.extractOne(query, pictograms[key]['search_keywords'])
        if score[1] >= 85:
            # Refine results
            if fuzz.partial_ratio(query, score[0]) >= 80:
                simple_ratio = fuzz.ratio(query, score[0])
                if simple_ratio >= 65:
                    results.append([
                        pictograms[key]['title'],
                        key,
                        score[1],
                        simple_ratio
                    ])
    return sorted(results, key=lambda x: (x[2], x[3]), reverse=True)[:limit]


###############################################################################
# BROWSE                                                                      #
###############################################################################
def browse(bot, update):
    """/browse command. Displays a keyboard/buttons UI for navigation.

    Catalog-like UI where the user can browse through different categories of
    pictograms.

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
    """
    # 1st level keyboard: main keyboard
    reply_markup = build_keyboard(keyboards['KB_MAIN']['layout'])
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=keyboards['KB_MAIN']['text'],
        reply_markup=reply_markup
    )


###############################################################################
# UNKNOWN COMMAND                                                             #
# Fall through                                                                #
###############################################################################
def unknown_command(bot, update):
    """Where the unknown commands come to die.

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
    """
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=error_messages['UNKNOWN_COMMAND']
    )
    help(bot, update)


###############################################################################
# UNKNOWN TYPE                                                                #
###############################################################################
def unknown_type(bot, update):
    """Unknown -Telegram- type handler.

    The bot only accepts text input. If any other data type is sent, it is
    rejected.

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
    """
    if update.message.audio:
        text = error_messages['UNKNOWN_TYPE_AUDIO']
    elif update.message.document:
        text = error_messages['UNKNOWN_TYPE_DOCUMENT']
    elif update.message.photo:
        text = error_messages['UNKNOWN_TYPE_PHOTO']
    elif update.message.sticker:
        text = error_messages['UNKNOWN_TYPE_STICKER']
    elif update.message.video:
        text = error_messages['UNKNOWN_TYPE_VIDEO']
    elif update.message.voice:
        text = error_messages['UNKNOWN_TYPE_VOICE']
    elif update.message.contact:
        text = error_messages['UNKNOWN_TYPE_CONTACT']
    elif update.message.location:
        text = error_messages['UNKNOWN_TYPE_LOCATION']
    elif update.message.venue:
        text = error_messages['UNKNOWN_TYPE_VENUE']
    else:
        text = error_messages['UNKNOWN_TYPE']
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=text
    )
    help(bot, update)


###############################################################################
# DISPATCH                                                                    #
###############################################################################
def dispatch(bot, update):
    """Handling of callbacks from inline keyboards

    Either send back another keyboard, a pictogram, or an error message

    Args:
        bot(object): the bot instance.
        update(object): the message sent by the user.
    """
    query = update.callback_query
    text = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    # Keyboards handling
    if text in keyboards:
        reply_markup = build_keyboard(keyboards[text]['layout'])
        bot.editMessageText(
            text=keyboards[text]['text'],
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=reply_markup
        )
    else:
        # Send pictogram
        if text in pictograms:
            send_picto(bot, chat_id, text)
        # Error / Something wrong
        else:
            bot.sendMessage(
                chat_id=chat_id,
                text=error_messages['PICTO_NOT_FOUND']
            )
    bot.answerCallbackQuery(callback_query_id=query.id)


###############################################################################
# KEYBOARDS                                                                   #
###############################################################################
def build_keyboard(kb_dict):
    """Builds a keyboard/buttons object from a dict

    Args:
        kbdict(dict): dict of buttons to display on the keyboard

    Returns:
        object: A keyboard formated for Telegram (InlineKeyboardMarkup)
    """
    # List of lists of InlineKeyboardButton built from dict argument
    inline_keyboard = []
    for text, callback_data in kb_dict.items():
        kb_button = [
            InlineKeyboardButton(
                text=text,
                callback_data=callback_data
            )
        ]
        inline_keyboard.append(kb_button)
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    )
    return reply_markup


###############################################################################
# IMAGES                                                                      #
###############################################################################
def send_picto(bot, chat_id, text):
    """Sends a pictogram to the user.

    Args:
        bot(object): the bot instance.
        chat_id(str): the id of the chat where the picto must be sent.
        text(str): the key of the dict corresponding to the picto to send.
    """
    bot.sendPhoto(
        chat_id=chat_id,
        photo=open(path_img + pictograms[text]['filename'], 'rb')
    )


###############################################################################
# ERRORS                                                                      #
###############################################################################
def error(bot, update, error):
    """Logs errors."""
    logger.warning('Update "%s" caused error "%s"' % (update, error))


###############################################################################
# MAIN                                                                        #
###############################################################################
def main():
    """Declaring handlers, start polling or webhook."""
    # updater = Updater(TOKEN, workers=16)
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start, pass_args=True))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('settings', settings))
    dp.add_handler(CommandHandler('browse', browse))
    dp.add_handler(CommandHandler('search', cmd_search, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, quick_search))
    dp.add_handler(MessageHandler(Filters.command, unknown_command))
    unknown_type_handler = MessageHandler(
        Filters.audio |
        Filters.document |
        Filters.photo |
        Filters.sticker |
        Filters.video |
        Filters.voice |
        Filters.contact |
        Filters.location,
        unknown_type
    )
    dp.add_handler(unknown_type_handler)
    dp.add_handler(InlineQueryHandler(inline_search))
    dp.add_handler(CallbackQueryHandler(dispatch))
    dp.add_error_handler(error)
    if ENV == 'local':
        # Test / GetUpdate
        updater.start_polling()
    else:
        # Production / Webhook
        updater.start_webhook(
            listen='0.0.0.0',
            port=PORT,
            url_path=TOKEN,
            webhook_url='https://%s/%s' % (HOST, TOKEN)
        )
        updater.bot.setWebhook('https://%s/%s' % (HOST, TOKEN))
    updater.idle()


if __name__ == '__main__':

    main()
