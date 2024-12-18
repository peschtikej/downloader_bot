from telebot.types import (
    Message,
)

from bot import bot
from django.conf import settings
from bot.text import FEEDBACK_TEXT

def feedback(message: Message):
    user_id = message.chat.id

    try:
        bot.send_message(chat_id=user_id, text=FEEDBACK_TEXT)
        
        bot.register_next_step_handler(message, waiting)

    except Exception as e:
        bot.send_message(user_id, 'We are currently fixing the bot. If this continues for too long, please use the command - /feedback')
        bot.send_message(settings.GROUP_ID, f'User {user_id} has an error during feedback: {e}')
        print(e)


def waiting(message: Message):
    user_id = message.chat.id
    user_text = message.text

    try:
        if user_text == "/cancel":
            bot.send_message(chat_id=user_id, text="Successfully canceled!")
            return


        if message.text:
            bot.send_message(chat_id=settings.GROUP_ID, text=f"User {user_id} sent feedback: {user_text}", parse_mode="Markdown")

        elif message.photo:
            bot.send_photo(chat_id=settings.GROUP_ID, photo=message.photo[-1].file_id, caption=f"User {user_id} sent feedback")

        elif message.video:
            bot.send_video(chat_id=settings.GROUP_ID, video=message.video.file_id, caption=f"User {user_id} sent feedback")

        elif message.voice:
            bot.send_voice(chat_id=settings.GROUP_ID, voice=message.voice.file_id, caption=f"User {user_id} sent feedback")

        elif message.video_note:
            bot.send_message(chat_id=settings.GROUP_ID, text=f"User {user_id} sent feedback:")
            bot.send_video_note(chat_id=settings.GROUP_ID, data=message.video_note.file_id)

        
        bot.send_message(chat_id=user_id, text="Thank you for your feedback!")
    
    except Exception as e:
        bot.send_message(user_id, 'We are currently fixing the bot. If this continues for too long, please use the command - /feedback')
        bot.send_message(settings.GROUP_ID, f'User {user_id} has an error during feedback: {e}')
        print(e)
