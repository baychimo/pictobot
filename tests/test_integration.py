#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from hypothesis import (
    given,
    settings
)
import hypothesis.strategies as st


@settings(deadline=3000, max_examples=20)
@given(
    msg=st.text(
        alphabet=st.characters(
            blacklist_categories=('Cc',),
            blacklist_characters='/ '),
        min_size=1
    )
)
def test_fuzz_str_input(userbot, msg):
    time.sleep(3)
    with userbot.conversation(userbot.get_entity('@Hal90Bot')) as conv:
        conv.send_message(msg)
        response = conv.get_response().raw_text
        # Unless we get very lucky and hypothesis generates something coherent:
        assert response.startswith('Sorry. No match found for') is True


@settings(deadline=3000, max_examples=20)
@given(
    msg=st.text(
        alphabet=st.characters(
            blacklist_categories=('Cc',)
        )
    )
)
def test_fuzz_cmd_input(userbot, msg):
    time.sleep(3)
    with userbot.conversation(userbot.get_entity('@Hal90Bot')) as conv:
        cmd = '/' + msg
        conv.send_message(cmd)
        response = conv.get_response().raw_text
        # Unless we get very lucky and hypothesis generates something coherent:
        assert response.startswith(
            'Sorry, I did not understand that command') is True
