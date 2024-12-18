from django.shortcuts import render

from traceback import format_exc

from asgiref.sync import sync_to_async
from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from telebot.types import Update
from telebot.apihelper import ApiTelegramException
from bot.handlers.common import *
from bot.handlers.user.feedback import feedback

from bot import bot

@require_GET
def set_webhook(request: HttpRequest) -> JsonResponse:
    """Setting webhook."""
    bot.set_webhook(url=f"{settings.HOOK}/bot/{settings.BOT_TOKEN}")
    bot.send_message(settings.OWNER_ID, "webhook set")
    return JsonResponse({"message": "OK"}, status=200)


@require_GET
def status(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"message": "OK"}, status=200)


@csrf_exempt
@require_POST
@sync_to_async
def index(request: HttpRequest) -> JsonResponse:
    if request.META.get("CONTENT_TYPE") != "application/json":
        return JsonResponse({"message": "Bad Request"}, status=403)

    json_string = request.body.decode("utf-8")
    update = Update.de_json(json_string)
    try:
        bot.process_new_updates([update])
    except ApiTelegramException as e:
        print(f"Telegram exception. {e} {format_exc()}")
    except ConnectionError as e:
        print(f"Connection error. {e} {format_exc()}")
    except Exception as e:
        bot.send_message(settings.OWNER_ID, f'Error from index: {e}')
        print(f"Unhandled exception. {e} {format_exc()}")
    return JsonResponse({"message": "OK"}, status=200)

"""
Common
"""
start = bot.message_handler(commands=["start"])(start)
help_ = bot.message_handler(commands=["help"])(help_)
feedback = bot.message_handler(commands=["feedback"])(feedback)