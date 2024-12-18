from bot import bot

from telebot.types import (
    Message,
)
from bot.text import START_TEXT, HELP_TEXT

def start(message: Message) -> None:
    """/start command handler"""

    user_id = message.from_user.id

    try:
        bot.send_message(
        chat_id=user_id,
        text=START_TEXT,
        parse_mode='Markdown'
        )

    except Exception as e:
        print(e)

def help_(message: Message) -> None:
    """/help command handler"""

    user_id = message.from_user.id

    try:
        bot.send_message(
        chat_id=user_id,
        text=HELP_TEXT,
        parse_mode='Markdown'
        )

    except Exception as e:
        print(e)