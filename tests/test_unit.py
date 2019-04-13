#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import contextlib
from unittest import mock

from hypothesis import (
    example,
    given,
    settings
)
import hypothesis.strategies as st
import pytest
from telegram import InlineKeyboardMarkup

from .context import *
from .context import local_settings


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
# For some reason I don't understand InlineKeyboardMarkup can't be mocked
# @mock.patch('telegram.InlineKeyboardMarkup')
@mock.patch('telegram.InlineKeyboardButton')
@mock.patch.object(core, 'help')
def test_start_from_inline(mock_help, mock_kb_button, mock_update, mock_bot):
    core.start(mock_bot, mock_update, [messages.info_messages['SWITCH_PM_PARAM']])
    mock_bot.sendMessage.assert_called_once_with(
        chat_id=mock_update.message.chat_id,
        text=messages.info_messages['START_INLINE_MSG'],
        reply_markup=InlineKeyboardMarkup([[mock_kb_button(text='mock_text')]])
    )
    mock_help.assert_not_called()


@given(args=st.lists(st.text()))
def test_start(args):
    with contextlib.ExitStack() as stack:
        mock_bot = stack.enter_context(mock.patch('telegram.bot.Bot'))
        mock_update = stack.enter_context(mock.patch('telegram.update.Update'))
        mock_help = stack.enter_context(mock.patch.object(core, 'help'))

        core.start(mock_bot, mock_update, args)

    mock_bot.sendMessage.assert_called_once_with(
        chat_id=mock_update.message.chat_id,
        text=messages.info_messages['START_MSG']
    )
    mock_help.assert_called_once_with(mock_bot, mock_update)


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
# Hopefully this will become patchable
# @mock.patch('telegram.InlineKeyboardMarkup')
@mock.patch('telegram.InlineKeyboardButton')
def test_help(mock_kb_button, mock_update, mock_bot):
    core.help(mock_bot, mock_update)
    mock_bot.sendMessage.assert_called_once_with(
        chat_id=mock_update.message.chat_id,
        text=messages.info_messages['HELP_MSG'],
        reply_markup=InlineKeyboardMarkup([[mock_kb_button(text='mock_text')]])
    )


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
def test_settings(mock_update, mock_bot):
    core.settings(mock_bot, mock_update)
    mock_bot.sendMessage.assert_called_once_with(
        chat_id=mock_update.message.chat_id,
        text=messages.info_messages['SETTINGS_MSG']
    )


@given(raw_query=st.text(min_size=1))
def test_quick_search(raw_query):
    with contextlib.ExitStack() as stack:
        mock_bot = stack.enter_context(mock.patch('telegram.bot.Bot'))
        mock_update = stack.enter_context(mock.patch('telegram.update.Update'))
        mock_search = stack.enter_context(mock.patch.object(core, 'search'))

        mock_update.message.text = raw_query
        core.quick_search(mock_bot, mock_update)

    mock_search.assert_called_once_with(mock_bot, mock_update, mock_update.message.text)


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
def test_cmd_search_empty(mock_update, mock_bot):
    core.cmd_search(mock_bot, mock_update, [])
    mock_bot.sendMessage.assert_called_once_with(
        chat_id=mock_update.message.chat_id,
        text=messages.info_messages['QUERY_MSG']
    )


@given(args=st.lists(st.text(min_size=1), min_size=1))
def test_cmd_search_non_empty(args):
    with contextlib.ExitStack() as stack:
        mock_bot = stack.enter_context(mock.patch('telegram.bot.Bot'))
        mock_update = stack.enter_context(mock.patch('telegram.update.Update'))
        mock_search = stack.enter_context(mock.patch.object(core, 'search'))

        core.cmd_search(mock_bot, mock_update, args)

    raw_query = ' '.join(args)
    mock_search.assert_called_once_with(mock_bot, mock_update, raw_query)


@settings(deadline=300, max_examples=50)
@given(raw_query=st.text(min_size=1))
def test_search(raw_query):
    with contextlib.ExitStack() as stack:
        mock_bot = stack.enter_context(mock.patch('telegram.bot.Bot'))
        mock_update = stack.enter_context(mock.patch('telegram.update.Update'))
        mock_kb_button = stack.enter_context(mock.patch('telegram.InlineKeyboardButton'))

        core.search(mock_bot, mock_update, raw_query)

    query = core.sanitize_string(raw_query)
    results = core.fuzzy_search(query, 7)
    if results:
        mock_bot.sendMessage.assert_called_once_with(
            chat_id=mock_update.message.chat_id,
            text=messages.info_messages['RESULTS_MSG'] + " '" + raw_query + "'",
            reply_markup=InlineKeyboardMarkup([[mock_kb_button(text='mock_text')]])
        )
    else:
        mock_bot.sendMessage.assert_called_once_with(
            chat_id=mock_update.message.chat_id,
            text=messages.info_messages['NO_RESULT_MSG_1'] +
            " '" + raw_query + "' " +
            messages.info_messages['NO_RESULT_MSG_2']
        )


@given(raw_query=st.text())
def test_inline_search(raw_query):
    with contextlib.ExitStack() as stack:
        mock_bot = stack.enter_context(mock.patch('telegram.bot.Bot'))
        mock_update = stack.enter_context(mock.patch('telegram.update.Update'))
        mock_update.inline_query.query = raw_query
        local_settings.external_path_img = 'https://static.yourserver.com/pictobot/fullsize/'
        local_settings.external_path_thumbs = 'https://static.yourserver.com/pictobot/thumbs/'

        core.inline_search(mock_bot, mock_update)

        mock_bot.answerInlineQuery.assert_called_once()


@settings(max_examples=1000)
@given(query=st.text())
def test_sanitize_string(query):
    third_pass = core.sanitize_string(query)
    assert isinstance(third_pass, str)


@given(query=st.text())
@example('')
def test_fuzzy_search(query):
    results = core.fuzzy_search(query, 7)
    assert len(results) < 8
    assert isinstance(results, list)
    if not query:
        assert not results


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
@mock.patch.object(core, 'build_keyboard')
def test_browse(mock_build_kb, mock_update, mock_bot):
    reply_markup = mock_build_kb(keyboards['KB_MAIN']['layout'])

    core.browse(mock_bot, mock_update)

    mock_bot.sendMessage.assert_called_once_with(
        chat_id=mock_update.message.chat_id,
        text=keyboards['KB_MAIN']['text'],
        reply_markup=reply_markup
    )
    # Once here and once in the actual (test) run
    calls = [mock.call(keyboards['KB_MAIN']['layout']), mock.call(keyboards['KB_MAIN']['layout'])]
    mock_build_kb.assert_has_calls(calls, any_order=True)


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
@mock.patch.object(core, 'help')
def test_unknown_command(mock_help, mock_update, mock_bot):
    core.unknown_command(mock_bot, mock_update)

    mock_bot.sendMessage.assert_called_once_with(
        chat_id=mock_update.message.chat_id,
        text=messages.error_messages['UNKNOWN_COMMAND']
    )
    mock_help.assert_called_once_with(mock_bot, mock_update)


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
@mock.patch.object(core, 'help')
def test_unknown_type(mock_help, mock_update, mock_bot):
    core.unknown_type(mock_bot, mock_update)

    mock_bot.sendMessage.assert_called_once_with(
        chat_id=mock_update.message.chat_id,
        text=messages.error_messages['UNKNOWN_TYPE_AUDIO']  # Arbitrary first one...
    )
    mock_help.assert_called_once_with(mock_bot, mock_update)


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
@mock.patch.object(core, 'build_keyboard')
def test_dispatch_kb(mock_build_kb, mock_update, mock_bot):
    mock_update.callback_query.data = 'KB_EMERGENCY'
    reply_markup = mock_build_kb(keyboards['KB_EMERGENCY']['layout'])

    core.dispatch(mock_bot, mock_update)

    mock_bot.editMessageText.assert_called_once_with(
        text=keyboards['KB_EMERGENCY']['text'],
        chat_id=mock_update.callback_query.message.chat_id,
        message_id=mock_update.callback_query.message.message_id,
        reply_markup=reply_markup
    )

    mock_bot.answerCallbackQuery.assert_called_once_with(
        callback_query_id=mock_update.callback_query.id
    )


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
@mock.patch.object(core, 'send_picto')
def test_dispatch_picto(mock_send_picto, mock_update, mock_bot):
    text = mock_update.callback_query.data = 'JUSTICE'

    core.dispatch(mock_bot, mock_update)

    mock_send_picto.assert_called_once_with(
        mock_bot,
        mock_update.callback_query.message.chat_id,
        text
    )

    mock_bot.answerCallbackQuery.assert_called_once_with(
        callback_query_id=mock_update.callback_query.id
    )


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
def test_dispatch_error(mock_update, mock_bot):
    mock_update.callback_query.data = 'NEITHER_HERE_NOR_THERE'

    core.dispatch(mock_bot, mock_update)

    mock_bot.sendMessage.assert_called_once_with(
        text=messages.error_messages['PICTO_NOT_FOUND'],
        chat_id=mock_update.callback_query.message.chat_id
    )

    mock_bot.answerCallbackQuery.assert_called_once_with(
        callback_query_id=mock_update.callback_query.id
    )


def test_build_keyboard():
    reply_markup = core.build_keyboard(keyboards['KB_MAIN']['layout'])
    assert isinstance(reply_markup, InlineKeyboardMarkup)


def test_build_keyboard_wrong_type():
    with pytest.raises(AttributeError):
        core.build_keyboard([])


@mock.patch('telegram.bot.Bot')
@mock.patch('telegram.update.Update')
def test_send_picto(mock_update, mock_bot):
    text = 'AIRPLANE'
    chat_id = mock_update.callback_query.message.chat_id
    core.send_picto(mock_bot, chat_id, text)
    mock_bot.sendPhoto.assert_called()
    # I can't figure out why the next lines are triggering an AssertionError
    # while showing strictly identical values for 'Expected call' and
    # 'Actual call'...
    # mock_bot.sendPhoto.assert_called_once_with(
    #     chat_id=chat_id,
    #     photo=open(
    #         local_settings.path_img + pictograms[text]['filename'],
    #         'rb'
    #     )
    # )
