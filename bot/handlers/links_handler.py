from telebot.types import (
    Message,
)

from bot.apis.links_handler import identify_service
from bot.handlers.user.ya_music import download_yandex_music_track_thread
from bot import bot
from django.conf import settings

def sending(message: Message):
    user_id = message.from_user.id
    
    try:
        service = identify_service(message.text)

        if service == "yandex_music":
            download_yandex_music_track_thread(message)
        
        else:
            bot.send_message(chat_id=user_id, text=service)
            bot.send_message(chat_id=user_id, text="Sorry, I don't support this service yet.", reply_to_message_id=message.message_id)
    
    except Exception as e:
        bot.send_message(user_id, 'We are currently fixing the bot. If this continues for too long, please use the command - /feedback')
        bot.send_message(settings.GROUP_ID, f'User {user_id} has an error during sending: {e}')
        print(e)