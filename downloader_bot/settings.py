import os

import dotenv
from os import getenv

from pathlib import Path
from telebot.types import BotCommand

dotenv.load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-ux=$ul=^eo+s=1m+vrrt637x&aab7nk4g1hvbb*v^n(3+4e!!o'

DEBUG = True

ALLOWED_HOSTS = ["*"]

BOT_TOKEN = getenv("BOT_TOKEN")
HOOK = getenv("HOOK")
HOOK = "https://fe04-178-176-167-194.ngrok-free.app"
OWNER_ID = getenv("OWNER_ID")
GROUP_ID = getenv("GROUP_ID")
YA_TOKEN = getenv("YA_TOKEN")

BOT_COMMANDS = [
    BotCommand("start", "Info"),
    BotCommand("help", "Help"),
    BotCommand("feedback", "Feedback"),
]

LINK_PATTERNS = {
        "tiktok": r"(https?://)?(www\.)?(tiktok\.com|tiktokv\.com|vm\.tiktok\.com|m\.tiktok\.com|tiktok\.me|vt\.tiktok\.com|link\.e\.tiktok\.com|us\.tiktok\.com|t\.tiktok\.com|oec-api\.tiktokv\.com|tt\.fun|tt\.inc|tt\.site|shop\.tiktok\.com|tokopedia\.com).*",
        "instagram": r"(https?://)?(www\.)?instagram\.com/.*",
        "youtube": r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.*",
        "spotify": r"(https?://)?(open\.)?spotify\.com/.*",
        "yandex_music": r"(https?://)?music\.yandex\.(ru|com)/album/\d+/track/\d+.*",
        "pinterest": r"(https?://)?(www\.)?(pinterest\.com/|pin\.it)/.*",
    }

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'downloader_bot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'downloader_bot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
