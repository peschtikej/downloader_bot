import os

from telebot.types import (
    Message,
)

from bot import bot
from django.conf import settings
from bot.apis.yandex_music import download_yandex_music_track

def download_yandex_music_track(message: Message):
    user_id = message.from_user.id

    try:
        bot.send_message(chat_id=user_id, text="Your request is being processed...", reply_to_message_id=message.message_id)

        file_path = download_yandex_music_track(message=message)

        with open(file_path, "rb") as music:
            bot.delete_message(chat_id=user_id, message_id=message.message_id)
            bot.send_audio(chat_id=user_id, audio=music, reply_to_message_id=message.message_id)

        os.remove(file_path)

    except Exception as e:
        bot.send_message(user_id, 'We are currently fixing the bot. If this continues for too long, please use the command - /feedback')
        bot.send_message(settings.GROUP_ID, f'User {user_id} has an error during download_yandex_music_track - user: {e}')
        print(e)