import asyncio
import os
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls import Exceptions

import config
from Arank_Music import LOGGER, YouTube, app
from Arank_Music.misc import db
from Arank_Music.utils.database import (
    add_active_chat,
    add_active_video_chat,
    get_lang,
    get_loop,
    group_assistant,
    is_autoend,
    music_on,
    remove_active_chat,
    remove_active_video_chat,
    set_loop,
)
from Arank_Music.utils.exceptions import AssistantErr
from Arank_Music.utils.formatters import check_duration, seconds_to_min, speed_converter
from Arank_Music.utils.inline.play import stream_markup
from Arank_Music.utils.stream.autoclear import auto_clean
from Arank_Music.utils.thumbnails import get_thumb
from strings import get_string

autoend = {}
counter = {}


class Call(PyTgCalls):
    def __init__(self):
        self.userbot1 = Client(
            name="Arank_Music",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
        )
