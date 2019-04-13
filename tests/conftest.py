#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess

import pytest
from telethon import TelegramClient, sync
from .context import local_settings


# @pytest.fixture(scope='session', autouse=True)
@pytest.fixture(scope='module')
def userbot():
    """
    Launch the userbot for the duration of the tests. The fixture above makes the userbot available
    to all the tests via the name "userbot"
    """
    # Start a bot so the userbot has someone to talk to
    bot = subprocess.Popen(
        ['python', '-W', 'ignore', os.path.join(local_settings.ROOT_DIR, 'core.py')]
    )
    client = TelegramClient('telethon', local_settings.API_ID, local_settings.API_HASH).start()
    yield client
    # Disconnect the userbot when all the tests are run
    client.disconnect()
    # Stop the bot
    bot.kill()
